import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:orquidia/application/use_cases/prediction_use_case.dart';
import 'package:orquidia/domain/models/prediction/prediction_input.dart';

// Events
abstract class InputEvent {}

class SubmitInputEvent extends InputEvent {
  final PredictionInput input;

  SubmitInputEvent({required this.input});
}

// States
abstract class InputState {}

class InputInitial extends InputState {}

class InputLoading extends InputState {}

class InputSuccess extends InputState {
  final String prediction;

  InputSuccess(this.prediction);
}

class InputFailure extends InputState {
  final String error;

  InputFailure(this.error);
}

// BLoC
class InputBloc extends Bloc<InputEvent, InputState> {
  final PredictionUseCase predictionUseCase;

  InputBloc(this.predictionUseCase) : super(InputInitial()) {
    // Register event handlers
    on<SubmitInputEvent>((event, emit) async {
      emit(InputLoading());
      try {
        // Execute the prediction use case
        String prediction = await predictionUseCase.execute(event.input);
        // Emit success state with the prediction result
        emit(InputSuccess(prediction));
      } catch (e) {
        // Emit failure state with the error message
        emit(InputFailure(e.toString()));
      }
    });
  }
}
