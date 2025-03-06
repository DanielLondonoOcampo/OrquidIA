import 'package:orquidia/domain/models/prediction/prediction_input.dart';

import '../repositories/prediction_repository.dart';

class PredictionUseCase {
  final PredictionRepository repository;

  PredictionUseCase(this.repository);

  Future<String> execute(PredictionInput input) {
    return repository.getPrediction(input);
  }
}
