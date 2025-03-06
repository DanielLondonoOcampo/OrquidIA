import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:go_router/go_router.dart';
import 'package:orquidia/domain/models/prediction/prediction_input.dart';
import 'package:orquidia/presentation/blocs/input_bloc.dart';
import 'package:orquidia/presentation/widgets/input_field.dart';

class FormScreen extends StatelessWidget {
  final List<TextEditingController> featureControllers = List.generate(
      7, (index) => TextEditingController()); // Adjusted to 7 controllers
  final List<String> featureNames = [
    "Anemia",
    "Creatinina",
    "Proteína en 24 horas",
    "Tipo de inmunoglobulina",
    "Cadena",
    "LDH",
    "FE"
  ];

  FormScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Input Data")),
      body: BlocConsumer<InputBloc, InputState>(
        listener: (context, state) {
          if (state is InputFailure) {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(content: Text('Error: ${state.error}')),
            );
          }
          if (state is InputSuccess) {
            GoRouter.of(context).go('/prediction', extra: state.prediction);
          }
        },
        builder: (context, state) {
          return Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              children: [
                for (int i = 0; i < featureNames.length; i++)
                  InputField(
                    featureController: featureControllers[i],
                    name: featureNames[i],
                  ),

                // Show CircularProgressIndicator if loading
                if (state is InputLoading)
                  const Center(child: CircularProgressIndicator()),
                const SizedBox(
                  height: 17,
                ),
                ElevatedButton(
                  onPressed: () {
                    // Call function to send data to the model
                    final PredictionInput input = PredictionInput(
                        anemia: featureControllers[0].text,
                        creat: featureControllers[1].text,
                        prot_24: featureControllers[2].text,
                        ig: featureControllers[3].text,
                        chain: featureControllers[4].text,
                        ldh: featureControllers[5].text,
                        fe: featureControllers[6].text);

                    BlocProvider.of<InputBloc>(context)
                        .add(SubmitInputEvent(input: input));
                  },
                  child: const Text("Predict"),
                ),
              ],
            ),
          );
        },
      ),
    );
  }
}
