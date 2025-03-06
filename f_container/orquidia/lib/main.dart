import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:go_router/go_router.dart';
import 'package:orquidia/application/repositories/prediction_repository.dart';
import 'package:orquidia/application/use_cases/prediction_use_case.dart';
// import 'package:orquidia/domain/models/prediction_output.dart';
import 'package:orquidia/presentation/blocs/input_bloc.dart';
import 'package:orquidia/presentation/config/theme/app_theme.dart';
import 'package:orquidia/presentation/screens/form/form_screen.dart';
// import 'package:orquidia/presentation/screens/home/home_screen.dart';
import 'package:orquidia/presentation/screens/prediction/prediction_screen.dart';

Future<void> main() async {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    final PredictionRepository predictionRepository =
        PredictionRepository(apiUrl: "http://localhost:8000/submit");
    final PredictionUseCase predictionUseCase =
        PredictionUseCase(predictionRepository);
    final GoRouter router = GoRouter(
      routes: [
        GoRoute(path: '/', builder: (context, state) => FormScreen(), routes: [
          GoRoute(
            path: '/prediction',
            builder: (context, state) =>
                PredictionScreen(prediction: state.extra as String),
          ),
        ]),
        // GoRoute(
        //   path: '/submit',
        //   builder: (context, state) => FormScreen(),
        // ),
      ],
    );

    return MultiBlocProvider(
      providers: [
        BlocProvider<InputBloc>(
          create: (BuildContext context) => InputBloc(predictionUseCase),
        ), //Problem here
      ],
      child: MaterialApp.router(
        routerConfig: router,
        title: 'MM Class Prediction',
        theme: AppTheme().getTheme(),
      ),
    );
  }
}
