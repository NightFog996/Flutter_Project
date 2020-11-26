import os,sys,re

admobinfo_path = '/Users/gsky/my_github/flutter_project/comm/admob_info.dart'
new_widgets_path = '/Users/gsky/my_github/flutter_project/comm/new_widgets'
my_file_path = '/Users/gsky/my_github/flutter_project/comm'

now_path = os.path.abspath('.')
# res_path = input("input your path: ")

test_app_id = 'ca-app-pub-3940256099942544~1458002511'


# 跳转到项目根目录
# os.chdir(res_path)
# print(os.path.abspath('.'))

# 修改文本的指定行; 找到old_text,并且在它上方插入new_text
def change_line(file_path,old_text,new_text):

    file = open( file_path, "r" ) 
    content = file.read() 
    pos = content.find( old_text)

    if pos != -1:
        print("找到了")
        content = content[:pos] + new_text + content[pos:] 
        file.close() 
        file = open( file_path, "w" ) 
        file.write( content ) 
        file.close() 
    else:
        print("没找到")


# 1. 修改pubspec.yaml内容
path = './pubspec.yaml'
change_line(path,'cupertino_icons','admob_flutter: ^0.3.4\n  dio: ^3.0.9\n  shared_preferences: ^0.5.10\n  ')

# 2. 修改 info.list内容
infoPlist_path = now_path + '/ios/Runner/Info.plist'
print(infoPlist_path)
old_info = '<key>CFBundleDevelopmentRegion'
new_info = '<key>GADApplicationIdentifier</key>\n<string>%s</string>\n<key>io.flutter.embedded_views_preview</key>\n<true/>\n' % test_app_id

change_line(infoPlist_path,old_info,new_info)


# 3. 复制admob_info.dart文件
# os.system("cp %s ./lib/admob_info.dart" % admobinfo_path )

# 4. 修改main文件
main_path = './lib/main.dart'
old_info = 'runApp'
new_info = 'Admob.initialize("%s"); \n  ' % test_app_id

change_line(main_path,old_info,new_info)

old_info = 'import'
new_info = 'import \'package:admob_flutter/admob_flutter.dart\';\n'
change_line(main_path,old_info,new_info)

old_info = 'int _counter = 0;'

new_info = '''

   GlobalKey<ScaffoldState> scaffoldState = GlobalKey();
  AdmobBannerSize bannerSize;
  AdmobInterstitial interstitialAd;
  
    @override
  void initState() {
    super.initState();
    bannerSize = AdmobBannerSize.BANNER;
    interstitialAd = AdmobInterstitial(
      adUnitId: "ca-app-pub-3940256099942544/4411468910",
      listener: (AdmobAdEvent event, Map<String, dynamic> args) {
        if (event == AdmobAdEvent.closed) interstitialAd.load();
        handleEvent(event, args, 'Interstitial');
      },
    );
    interstitialAd.load();
  }
  
void handleEvent(
      AdmobAdEvent event, Map<String, dynamic> args, String adType) {
    switch (event) {
      case AdmobAdEvent.loaded:
        print('New Admob $adType Ad loaded!');
        break;
      case AdmobAdEvent.opened:
        print('Admob $adType Ad opened!');
        break;
      case AdmobAdEvent.closed:
        print('Admob $adType Ad closed!');
        break;
      case AdmobAdEvent.failedToLoad:
        print('Admob $adType failed to load. :(');
        break;
      default:
    }
  }
  
  //使用横幅,直接当控件使用;
//      AdmobBanner(
//               adUnitId: "ca-app-pub-3940256099942544/2934735716",
//               adSize: bannerSize,
//               listener: (AdmobAdEvent event, Map<String, dynamic> args) {
//                 handleEvent(event, args, 'Banner');
//               },
//             ),

//使用插页的按钮

//       onPressed: () async {
//           if (await interstitialAd.isLoaded) {
//             interstitialAd.show();
//           } else {
//             print("Interstitial ad is still loading...");
//           }
//         },
  
'''

change_line(main_path,old_info,new_info)



# 5. 复制自定义控件
# os.system("cp  -r %s ./lib/" % new_widgets_path )

# 6. 复制我的自定义类
os.system("cp  -r %s ./lib/" % my_file_path )