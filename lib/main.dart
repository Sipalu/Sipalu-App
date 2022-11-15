import 'package:flutter/material.dart';
import 'package:sipalu/screens/homePage.dart';
import 'package:sipalu/screens/loginPage.dart';
import 'package:sipalu/screens/registerPage.dart';

void main(List<String> args) {
  runApp(
    MaterialApp(
      debugShowCheckedModeBanner: false,
      routes: {
        '/loginPage': (context) => const LoginPageScreen(),
        '/registerPage': (context) => const RegisterPageScreen(),
        '/homePage': (context) => const HomePageScreen()
      },
      initialRoute: '/loginPage',
    ),
  );
}
