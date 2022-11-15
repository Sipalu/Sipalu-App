import 'dart:convert';

import 'package:flutter/material.dart';

import 'package:http/http.dart' as http;
import 'package:motion_toast/motion_toast.dart';
import 'package:sipalu/utils/url.dart';

class RegisterPageScreen extends StatefulWidget {
  const RegisterPageScreen({Key? key}) : super(key: key);

  @override
  State<RegisterPageScreen> createState() => _RegisterPageScreenState();
}

class _RegisterPageScreenState extends State<RegisterPageScreen> {
  var nameController = TextEditingController();
  var addressController = TextEditingController();
  var emailController = TextEditingController();
  var passwordController = TextEditingController();

  var statusReceived;

  Future submit() async {
    http.Response response;
    response = await http.post(
      Uri.parse("$baseUrl/account/register"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode(
        <String, String>{
          'name': nameController.text,
          'address': addressController.text,
          'email': emailController.text,
          'password': passwordController.text
        },
      ),
    );

    if (response.statusCode == 200) {
      setState(() {
        var registerResponse = json.decode(response.body);
        statusReceived = registerResponse["foundResponse"];
      });
    }
    if (statusReceived == "1") {
      MotionToast(
              primaryColor: Colors.green,
              width: 320,
              title: const Text("Success!"),
              description: const Text("Registered Successfully"),
              icon: Icons.login_rounded)
          .show(context);
    } else {
      MotionToast(
              primaryColor: Colors.red,
              width: 320,
              title: const Text("Failure!"),
              description: const Text("Failed To Register!"),
              icon: Icons.login_rounded)
          .show(context);
    }
  }

  clear() {
    setState(() {
      nameController.clear();
      emailController.clear();
      addressController.clear();
      passwordController.clear();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        height: double.infinity,
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topRight,
            end: Alignment.bottomLeft,
            colors: [
              Color.fromARGB(255, 125, 151, 201),
              Color.fromARGB(255, 59, 161, 65),
            ],
          ),
        ),
        child: SafeArea(
          child: Center(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(20, 0, 20, 0),
              child: SingleChildScrollView(
                child: Column(
                  children: [
                    Text(
                      "Join Us Today!",
                      style: TextStyle(
                          color: Colors.grey[800],
                          fontWeight: FontWeight.w900,
                          fontStyle: FontStyle.italic,
                          fontFamily: 'Open Sans',
                          fontSize: 40),
                    ),
                    const SizedBox(
                      height: 20,
                    ),
                    const Text(
                      "Full Name:",
                      style: TextStyle(fontSize: 20),
                    ),
                    TextFormField(
                      controller: nameController,
                    ),
                    const SizedBox(
                      height: 20,
                    ),
                    const Text(
                      "Address:",
                      style: TextStyle(fontSize: 20),
                    ),
                    TextFormField(
                      controller: addressController,
                    ),
                    const SizedBox(
                      height: 20,
                    ),
                    const Text(
                      "Email:",
                      style: TextStyle(fontSize: 20),
                    ),
                    TextFormField(
                      controller: emailController,
                    ),
                    const SizedBox(
                      height: 20,
                    ),
                    const Text(
                      "Password:",
                      style: TextStyle(fontSize: 20),
                    ),
                    TextFormField(
                      controller: passwordController,
                    ),
                    const SizedBox(
                      height: 10,
                    ),
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: [
                        ElevatedButton(
                          style:
                              ElevatedButton.styleFrom(primary: Colors.green),
                          onPressed: () {
                            submit();
                            clear();
                          },
                          child: const Icon(Icons.app_registration_rounded),
                        ),
                        ElevatedButton(
                          style: ElevatedButton.styleFrom(primary: Colors.red),
                          onPressed: () {
                            clear();
                          },
                          child: const Icon(Icons.delete_rounded),
                        ),
                        TextButton(
                          onPressed: () {
                            Navigator.pushNamed(context, '/loginPage');
                          },
                          child: const Text(
                            "Login",
                            style: TextStyle(color: Colors.yellow),
                          ),
                        )
                      ],
                    ),
                    const SizedBox(
                      height: 10,
                    )
                  ],
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}
