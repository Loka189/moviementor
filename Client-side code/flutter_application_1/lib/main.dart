import 'dart:convert';
import 'package:flutter_application_1/ani.dart';
import 'package:flutter_application_1/rough.dart';
import 'package:simple_gradient_text/simple_gradient_text.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter Demo',
      debugShowCheckedModeBanner: false,
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key});

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var movieNameController = TextEditingController();
  List movie_names = [];
  List movie_posters = [];
  // Color changing effect
  Color redColor = Colors.red;
  Color yellowColor = Colors.yellowAccent;
  //Color containerColor = Colors.red;
  bool isSwitched = false;

  late StreamSubscription<bool> colorChangeSubscription;

  Stream<bool> colorChangeStream() async* {
    while (true) {
      await Future.delayed(Duration(seconds: 2));
      yield !isSwitched;
      isSwitched = !isSwitched;
    }
  }

  @override
  void initState() {
    super.initState();
    colorChangeSubscription = colorChangeStream().listen((shouldChange) {
      if (shouldChange) {
        setState(() {
          redColor = Colors.yellowAccent;
          yellowColor = Colors.red;
        });
      } else {
        setState(() {
          redColor = Colors.red;
          yellowColor = Colors.yellowAccent;
        });
      }
    });
  }

  @override
  void dispose() {
    colorChangeSubscription.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: MediaQuery.of(context).size.width,
        height: MediaQuery.of(context).size.height,
        color: const Color.fromARGB(255, 2, 17, 28),
        child: Column(
          children: [
            InkWell(
              onTap: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) {
                  return Ani();
                }));
              },
              child: Container(
                margin: const EdgeInsets.fromLTRB(0, 20, 0, 0),
                height: 100,
                width: MediaQuery.of(context).size.width,
                //color: Colors.red,
                child: Row(
                  children: [
                    const SizedBox(
                      width: 20,
                    ),
                    AnimatedContainer(
                      duration: Duration(seconds: 2),
                      padding: const EdgeInsets.all(2),
                      height: 100,
                      width: 200,
                      decoration: BoxDecoration(
                          gradient: LinearGradient(
                              colors: [redColor, yellowColor],
                              begin: Alignment.topRight,
                              end: Alignment.bottomLeft),
                          borderRadius: BorderRadius.circular(16)),
                      child: Container(
                        width: double.infinity,
                        height: double.infinity,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(16),
                          color: const Color.fromARGB(255, 2, 17, 28),
                        ),
                        child: Row(
                          children: [
                            AnimatedContainer(
                              duration: Duration(seconds: 2),
                              margin: EdgeInsets.fromLTRB(7.5, 0, 0, 0),
                              width: 80,
                              height: 80,
                              decoration: BoxDecoration(
                                  gradient: LinearGradient(
                                      colors: [redColor, yellowColor],
                                      begin: Alignment.topRight,
                                      end: Alignment.bottomLeft),
                                  borderRadius: BorderRadius.circular(16)),
                              child: const Center(
                                child: Text(
                                  'M',
                                  style: TextStyle(
                                      fontSize: 60,
                                      color: Color.fromARGB(255, 2, 17, 28),
                                      fontWeight: FontWeight.bold),
                                ),
                              ),
                            ),
                            const SizedBox(
                              width: 5,
                            ),
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                const SizedBox(
                                  height: 10,
                                ),
                                GradientText(
                                    colors: [redColor, yellowColor],
                                    'OVIE',
                                    style: const TextStyle(
                                        fontSize: 30,
                                        fontWeight: FontWeight.bold)),
                                AnimatedDefaultTextStyle(
                                  duration: Duration(seconds: 2),
                                  style: TextStyle(),
                                  child: GradientText(
                                    colors: [redColor, yellowColor],
                                    'ENTOR',
                                    style: const TextStyle(
                                        fontSize: 30,
                                        color: Color.fromARGB(255, 2, 17, 28),
                                        fontWeight: FontWeight.bold),
                                  ),
                                )
                              ],
                            )
                          ],
                        ),
                      ),
                    ),
                    const SizedBox(
                      width: 100,
                    ),
                    // Container(
                    //   padding: const EdgeInsets.all(2),
                    //   height: 100,
                    //   width: 200,
                    //   decoration: BoxDecoration(
                    //       gradient: const LinearGradient(
                    //           colors: [
                    //             Color(0xffb8f6fa),
                    //             Color(0xffa9ebf3),
                    //             Color(0xff87d0e3),
                    //             Color(0xff63b2d2),
                    //             Color(0xff3d89ba),
                    //             Color(0xff1b3c88),
                    //           ],
                    //           begin: Alignment.topRight,
                    //           end: Alignment.bottomLeft),
                    //       borderRadius: BorderRadius.circular(16)),
                    //   child: Container(
                    //     width: double.infinity,
                    //     height: double.infinity,
                    //     decoration: BoxDecoration(
                    //       borderRadius: BorderRadius.circular(16),
                    //       color: const Color.fromARGB(255, 2, 17, 28),
                    //     ),
                    //     child: Row(
                    //       children: [
                    //         Container(
                    //           margin: EdgeInsets.fromLTRB(7.5, 0, 0, 0),
                    //           width: 80,
                    //           height: 80,
                    //           decoration: BoxDecoration(
                    //               gradient: const LinearGradient(
                    //                   colors: [
                    //                     Color(0xffb8f6fa),
                    //                     Color(0xffa9ebf3),
                    //                     Color(0xff87d0e3),
                    //                     Color(0xff63b2d2),
                    //                     Color(0xff3d89ba),
                    //                     Color(0xff1b3c88),
                    //                   ],
                    //                   begin: Alignment.topRight,
                    //                   end: Alignment.bottomLeft),
                    //               borderRadius: BorderRadius.circular(16)),
                    //           child: const Center(
                    //             child: Text(
                    //               'M',
                    //               style: TextStyle(
                    //                   fontSize: 60,
                    //                   color: Color.fromARGB(255, 2, 17, 28),
                    //                   fontWeight: FontWeight.bold),
                    //             ),
                    //           ),
                    //         ),
                    //         const SizedBox(
                    //           width: 5,
                    //         ),
                    //         Column(
                    //           crossAxisAlignment: CrossAxisAlignment.start,
                    //           children: [
                    //             const SizedBox(
                    //               height: 10,
                    //             ),
                    //             GradientText(
                    //                 colors: [
                    //                   Color(0xffb8f6fa),
                    //                   Color(0xffa9ebf3),
                    //                   Color(0xff87d0e3),
                    //                   Color(0xff63b2d2),
                    //                   Color(0xff3d89ba),
                    //                   Color(0xff1b3c88),
                    //                 ],
                    //                 'OVIE',
                    //                 style: const TextStyle(
                    //                     fontSize: 30,
                    //                     fontWeight: FontWeight.bold)),
                    //             GradientText(
                    //               colors: [
                    //                 Color(0xffb8f6fa),
                    //                 Color(0xffa9ebf3),
                    //                 Color(0xff87d0e3),
                    //                 Color(0xff63b2d2),
                    //                 Color(0xff3d89ba),
                    //                 Color(0xff1b3c88),
                    //               ],
                    //               'ENTOR',
                    //               style: const TextStyle(
                    //                   fontSize: 30,
                    //                   color: Color.fromARGB(255, 2, 17, 28),
                    //                   fontWeight: FontWeight.bold),
                    //             )
                    //           ],
                    //         )
                    //       ],
                    //     ),
                    //   ),
                    // ),
                    // // Container(

                    //   color: Colors.yellowAccent,
                    //   width: 200,
                    //   child: Text(
                    //     'MovieMentor',
                    //     style: TextStyle(  rgb(176, 240, 246)
                    //         color: Colors.white,
                    //         fontSize: 20,
                    //         fontWeight: FontWeight.bold),
                    //   ),
                    // )
                  ],
                ),
              ),
            ),
            const SizedBox(
              height: 50,
            ),
            Container(
              padding: EdgeInsets.all(2),
              width: 500,
              height: 50,
              decoration: BoxDecoration(
                  // gradient: const LinearGradient(
                  //     colors: [Colors.red, Colors.yellowAccent],
                  //     begin: Alignment.topRight,
                  //     end: Alignment.bottomLeft),
                  borderRadius: BorderRadius.circular(20)),
              child: Container(
                width: double.infinity,
                height: double.infinity,
                decoration: BoxDecoration(
                  borderRadius: BorderRadius.circular(16),
                  color: const Color.fromARGB(255, 2, 17, 28),
                ),
                child: TextField(
                  style: const TextStyle(color: Colors.white),
                  controller: movieNameController,
                  decoration: InputDecoration(
                    hintText: 'Enter Movie Name',
                    hintStyle: const TextStyle(color: Colors.white60),
                    border: OutlineInputBorder(
                        borderSide: const BorderSide(color: Colors.cyanAccent),
                        borderRadius: BorderRadius.circular(20)),
                    enabledBorder: OutlineInputBorder(
                      borderSide: const BorderSide(color: Colors.cyanAccent),
                      borderRadius: BorderRadius.circular(20),
                    ),
                    focusedBorder: OutlineInputBorder(
                      borderSide: const BorderSide(color: Colors.cyanAccent),
                      borderRadius: BorderRadius.circular(20),
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(
              height: 20,
            ),
            ElevatedButton(
                style: ButtonStyle(
                    backgroundColor:
                        MaterialStatePropertyAll(Colors.deepOrange)),
                onPressed: () async {
                  var movieName = movieNameController.text;
                  var obj = recommendMovies(movieName);
                  var x = await obj.fetchRecommendations();
                  setState(() {
                    movie_names = x['movie_names'];
                    movie_posters = x['movie_posters'];
                  });
                },
                child: const Text('Recommend')),
            SizedBox(
              height: 10,
            ),
            // Container(
            //   padding: EdgeInsets.all(2),
            //   height: 35,
            //   width: 120,
            //   decoration: BoxDecoration(
            //     borderRadius: BorderRadius.circular(12),
            //     gradient: const LinearGradient(
            //         colors: [Colors.red, Colors.yellowAccent],
            //         begin: Alignment.topRight,
            //         end: Alignment.bottomLeft),
            //   ),
            //   child: Container(
            //     width: double.infinity,
            //     height: double.infinity,
            //     decoration: BoxDecoration(
            //       borderRadius: BorderRadius.circular(12),
            //       color: const Color.fromARGB(255, 2, 17, 28),
            //     ),
            //     child: Center(
            //       child: GradientText('RECOMMEND',
            //           colors: const [Colors.red, Colors.yellowAccent],
            //           style: const TextStyle(
            //               fontSize: 15, fontWeight: FontWeight.w500)),
            //     ),
            //   ),
            // ),
            const SizedBox(
              height: 40,
            ),
            Container(
              width: 1190,
              height: 350,
              //color: Colors.amber,
              child: Column(
                children: [
                  Expanded(
                      child: ListView.builder(
                    itemCount: movie_names.length,
                    scrollDirection: Axis.horizontal,
                    itemBuilder: (context, index) {
                      return Container(
                        margin: const EdgeInsets.symmetric(horizontal: 15),
                        //color: Colors.red,
                        width: 204,
                        child: Column(
                          children: [
                            Image.network(
                              movie_posters[index],
                              height: 285,
                              width: 200,
                              fit: BoxFit.cover,
                            ),
                            const SizedBox(
                              height: 10,
                            ),
                            Text(
                              movie_names[index],
                              style: const TextStyle(
                                  color: Colors.white, fontSize: 18),
                            )
                          ],
                        ),
                      );
                    },
                  ))
                ],
              ),
            )
            // Expanded(
            //   child: ListView.builder(
            //       scrollDirection: Axis.horizontal,
            //       itemCount: movie_names.length,
            //       padding: EdgeInsets.symmetric(horizontal: 220),
            //       itemBuilder: (context, index) {
            //         return Container(
            //           height: 150,
            //           width: 150,
            //           //color: Colors.red,
            //           child: Column(
            //             children: [
            //               Container(
            //                 height: 200,
            //                 width: 200,
            //                 child: Image.network(movie_posters[index]),
            //               ),
            //               SizedBox(
            //                 width: 20,
            //               ),
            //               Container(
            //                 height: 100,
            //                 width: 100,
            //                 child: Text(
            //                   movie_names[index],
            //                   style: TextStyle(color: Colors.white),
            //                 ),
            //               )
            //             ],
            //           ),
            //         );
            //       }),
            // )
          ],
        ),
      ),
    );
  }
}

class recommendMovies {
  var movie_name;
  recommendMovies(this.movie_name);
  Future<Map> fetchRecommendations() async {
    final apiUrl =
        'http://127.0.0.1:5000/get_recommendations?movie=$movie_name';
    final response = await http.get(Uri.parse(apiUrl));

    if (response.statusCode == 200) {
      final recommendations = response.body;
      List data = jsonDecode(recommendations);
      List movie_names = [];
      List movie_posters = [];
      Map movie_details = {
        'movie_names': movie_names,
        'movie_posters': movie_posters
      };
      for (var i = 0; i < data.length; i++) {
        movie_names.add(data[i]['title']);
        movie_posters.add(data[i]['imageurl']);
      }
      return movie_details;
    } else {
      Map error = {'error': 'Failed to fetch recommendations'};
      return error;
    }
  }
}
// import 'dart:async';
// import 'package:flutter/material.dart';
// import 'package:flutter_application_1/rough.dart';

// void main() {
//   runApp(MyApp());
// }

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       home: ColorChangeScreen(),
//     );
//   }
// }

// class ColorChangeScreen extends StatefulWidget {
//   @override
//   _ColorChangeScreenState createState() => _ColorChangeScreenState();
// }

// class _ColorChangeScreenState extends State<ColorChangeScreen> {
//   bool isSwitched = false;
//   Color mainBgColor = Colors.white;
//   Color mainTextColorB = Colors.black;
//   Color textColorW = Colors.white;
//   Color iconColor = Colors.black;
//   Color buttonContainerColor = const Color.fromARGB(255, 237, 235, 235);

//   late StreamSubscription<Color> colorSubscription;

//   Stream<Color> colorStream() async* {
//     while (true) {
//       await Future.delayed(Duration(seconds: 2));
//       yield isSwitched
//           ? const Color.fromARGB(255, 27, 26, 26)
//           : const Color.fromARGB(255, 237, 235, 235);
//       isSwitched = !isSwitched;
//     }
//   }

//   @override
//   void initState() {
//     super.initState();
//     colorSubscription = colorStream().listen((color) {
//       setState(() {
//         buttonContainerColor = color;
//         mainBgColor = isSwitched ? Colors.black : Colors.white;
//         mainTextColorB = isSwitched ? Colors.white : Colors.black;
//         textColorW = isSwitched ? Colors.black : Colors.white;
//         iconColor = isSwitched ? Colors.white : Colors.black;
//       });
//     });
//   }

//   @override
//   void dispose() {
//     colorSubscription.cancel();
//     super.dispose();
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       backgroundColor: mainBgColor,
//       appBar: AppBar(
//         title: Text("Color Change Demo"),
//       ),
//       body: Center(
//         child: Column(
//           mainAxisAlignment: MainAxisAlignment.center,
//           children: <Widget>[
//             InkWell(
//               onTap: () {
//                 Navigator.push(context, MaterialPageRoute(builder: (context) {
//                   return Rough();
//                 }));
//               },
//               child: Text(
//                 "Text Color: " + (isSwitched ? "White" : "Black"),
//                 style: TextStyle(color: mainTextColorB),
//               ),
//             ),
//             Icon(
//               Icons.palette,
//               color: iconColor,
//               size: 50.0,
//             ),
//             Container(
//               color: buttonContainerColor,
//               padding: EdgeInsets.all(20.0),
//               child: Text(
//                 "Button Container",
//                 style: TextStyle(color: textColorW),
//               ),
//             ),
//           ],
//         ),
//       ),
//     );
//   }
// }
