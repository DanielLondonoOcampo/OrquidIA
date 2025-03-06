import 'package:flutter/material.dart';

class PredictionScreen extends StatelessWidget {
  final String prediction;
  const PredictionScreen({super.key, required this.prediction});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Predicted class is $prediction"),
      ),
      body: Center(
        child: Text(prediction),
      ),
    );
  }
}
