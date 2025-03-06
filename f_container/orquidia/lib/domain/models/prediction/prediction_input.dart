// lib/domain/models/prediction_input.dart

class PredictionInput {
  final String anemia;
  final String creat;
  final String prot_24;
  final String ig;
  final String chain;
  final String ldh;
  final String fe;

  PredictionInput(
      {required this.anemia,
      required this.creat,
      required this.prot_24,
      required this.ig,
      required this.chain,
      required this.ldh,
      required this.fe});

  Map<String, String> toJson() {
    return {
      "anemia": anemia,
      "creat": creat,
      "prot_24": prot_24,
      "ig": ig,
      "chain": chain,
      "ldh": ldh,
      "fe": fe,
    };
  }
}
