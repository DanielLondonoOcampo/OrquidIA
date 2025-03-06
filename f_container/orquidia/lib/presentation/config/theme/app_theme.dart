import "package:flutter/material.dart";

const colorsList = <Color>[
  Colors.blue,
  Colors.teal,
  Colors.green,
  Colors.red,
  Colors.purple,
  Colors.deepPurple,
  Colors.deepPurpleAccent,
  Colors.orange,
];

class AppTheme {
  final int selectedColor;

  AppTheme({this.selectedColor = 0})
      : assert(selectedColor >= 0, "Selected color must be greather than 0"),
        assert(selectedColor < colorsList.length - 1,
            "Selected color must be less than or equal ${colorsList.length - 1}");

  ThemeData getTheme() => ThemeData(colorSchemeSeed: colorsList[selectedColor]);
}
