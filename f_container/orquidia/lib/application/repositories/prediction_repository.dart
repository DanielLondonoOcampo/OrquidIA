import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:orquidia/domain/models/prediction/prediction_input.dart';

class PredictionRepository {
  final String apiUrl;

  PredictionRepository({required this.apiUrl});

  Future<String> getPrediction(PredictionInput input) async {
    final response =
        await http.post(Uri.parse(apiUrl), // Update with your endpoint
            headers: {'Content-Type': 'application/json'},
            body: json.encode({
              "anemia": input.anemia,
              "creat": input.creat,
              "prot_24": input.prot_24,
              "ig": input.ig,
              "chain": input.chain,
              "ldh": input.ldh,
              "fe": input.fe
            }));

    if (response.statusCode == 200) {
      final responseData = jsonDecode(response.body);
      return responseData[
          'predicted_class']; // Adjust based on your API response structure
    } else {
      throw Exception('Failed to load prediction');
    }
  }
}
