import 'package:flutter/material.dart';

class TextWidget extends StatefulWidget {
  TextWidget(Key key) : super(key: key);

  @override
  State<StatefulWidget> createState() {
    return TextWidgetState();
  }
}

class TextWidgetState extends State<TextWidget> {
  String _text="0";

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(_text,style: TextStyle(fontSize: 20),),
    );
  }

  void onPressed(String count) {
    setState(() {
      print("显示答案: $count");
      _text = count;
    });
  }
}