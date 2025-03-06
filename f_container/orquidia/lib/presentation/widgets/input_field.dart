import 'package:flutter/material.dart';

class InputField extends StatelessWidget {
  final TextEditingController featureController;
  final String name;

  const InputField({
    super.key,
    required this.featureController,
    required this.name,
  });

  @override
  Widget build(BuildContext context) {
    return TextField(
      controller: featureController,
      decoration: InputDecoration(labelText: name),
    );
  }
}
