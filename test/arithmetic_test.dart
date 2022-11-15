import 'package:flutter_test/flutter_test.dart';
import 'package:fluttertest/model/Arithmatic.dart';

void main() {
      final arithmetic = Arithmetic();
      arithmetic.first = 4;
      arithmetic.second = 3;
  group('Arithmetic test', (){
    test('add two numbers', (){
    int expectedValue = 7;
    int actualValue = arithmetic.add();
    expect(actualValue, expectedValue);

    test('subtracting two numbers',() {
    int expectedValue = 3;
    int actualValue = arithmetic.sub();
     expect(actualValue, expectedValue);
  });

    });
  });


  test('multiplying two numbers', (){
    int expectedValue = 12;
    int actualValue = arithmetic.mul();
    expect(actualValue, expectedValue);
  });
}