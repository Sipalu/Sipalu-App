import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:motion_toast/motion_toast.dart';

import 'package:http/http.dart' as http;
import 'package:sipalu/utils/url.dart';

class LoginPageScreen extends StatefulWidget {
  const LoginPageScreen({Key? key}) : super(key: key);

  @override
  State<LoginPageScreen> createState() => _LoginPageScreenState();
}

class _LoginPageScreenState extends State<LoginPageScreen> {
  var emailController = TextEditingController();
  var passwordController = TextEditingController();
  var statusReceived;

  Future authentication() async {
    http.Response response;

    // response = await http.post(Uri.parse("$baseUrl/account/login"),
    response = await http.post(
      Uri.parse("$baseUrl/account/login"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode(
        <String, String>{
          'email': emailController.text,
          'password': passwordController.text
        },
      ),
    );

    if (response.statusCode == 200) {
      setState(() {
        var loginResponse = json.decode(response.body);
        // userID = loginResponse["userID"];
        statusReceived = loginResponse["foundResponse"];
        // signal = statusReceived == "1" ? true : false;
      });
      if (statusReceived == "1") {
        Navigator.pushNamed(context, '/homePage');
        MotionToast(
                primaryColor: Colors.green,
                width: 320,
                title: const Text("Welcome!"),
                description: const Text("Logged In Successfully"),
                icon: Icons.login_rounded)
            .show(context);
      } else if (statusReceived == "2") {
        MotionToast(
                primaryColor: Colors.red,
                width: 320,
                title: const Text("Wrong Password"),
                description: const Text("Password is invalid!"),
                icon: Icons.login_rounded)
            .show(context);
      } else {
        MotionToast(
                primaryColor: Colors.red,
                width: 320,
                title: const Text("Failed"),
                description: const Text("Invalid Credentials!"),
                icon: Icons.login_rounded)
            .show(context);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Container(
          //   child: Image.asset('assets/images/loginBg.jpg'),
          // ),
          Container(
            decoration: const BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topRight,
                end: Alignment.bottomLeft,
                colors: [
                  Colors.blue,
                  Colors.red,
                ],
              ),
            ),
            child: Padding(
              padding: const EdgeInsets.all(18.0),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Text(
                    "Welcome",
                    style: TextStyle(
                        color: Colors.grey[800],
                        fontWeight: FontWeight.w900,
                        fontStyle: FontStyle.italic,
                        fontFamily: 'Open Sans',
                        fontSize: 40),
                  ),
                  const SizedBox(
                    height: 40,
                  ),
                  const Text(
                    "Username:",
                    style: TextStyle(fontSize: 20),
                  ),
                  TextFormField(controller: emailController),
                  const SizedBox(
                    height: 20,
                  ),
                  const Text(
                    "Password:",
                    style: TextStyle(fontSize: 20),
                  ),
                  TextFormField(controller: passwordController),
                  const SizedBox(
                    height: 10,
                  ),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                    children: [
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(primary: Colors.green),
                        onPressed: () {
                          authentication();
                        },
                        child: const Icon(Icons.login_rounded),
                      ),
                      ElevatedButton(
                        style: ElevatedButton.styleFrom(primary: Colors.red),
                        onPressed: () {
                          emailController.clear();
                          passwordController.clear();
                        },
                        child: const Icon(Icons.delete),
                      ),
                      TextButton(
                        onPressed: () {
                          Navigator.pushNamed(context, '/registerPage');
                        },
                        child: const Text(
                          "Register Today!",
                          style: TextStyle(color: Colors.yellow),
                        ),
                      )
                    ],
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
