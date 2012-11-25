require 'formula'

class Aquaterm <Formula
  url 'http://downloads.sourceforge.net/project/aquaterm/AquaTerm/v1.0.1/aquaterm_src.1.0.1.tar.gz'
  homepage 'http://aquaterm.sourceforge.net/'
  md5 'e9d3ecdfe770d6f09a748add9886d1a9'

  def patches
    DATA
  end

  def install
    apppath = prefix + 'Applications'
    frameworkpath = prefix + 'Library/Frameworks'
    includepath = include + 'aquaterm'
    libs = [ 'libaquaterm.dylib', "libaquaterm.#{version}.dylib" ].map { |l| lib + l }
    headers = [ 'AQTAdapter.h', 'aquaterm.h' ].map { |h| includepath + h }

    Dir.chdir('aquaterm') do
      # Modify framework and application search paths
      inreplace "AquaTerm.xcodeproj/project.pbxproj" do |s|
        s.gsub! '$(LOCAL_LIBRARY_DIR)/Frameworks', frameworkpath
        s.gsub! '$(USER_APPS_DIR)', apppath
      end

      # Build app and framework
      system "xcodebuild", "-target", "AquaTerm", "-configuration", "Deployment"

      # Install app
      apppath.install 'build/Deployment/AquaTerm.app'

      # Install framework
      frameworkpath.install 'build/Deployment/AquaTerm.framework'

      # Install libs
      lib.mkpath
      libs.each do |l|
        l.make_link frameworkpath + 'AquaTerm.framework/AquaTerm'
      end

      # Install includes
      includepath.mkpath
      headers.each do |h|
        h.make_link frameworkpath + 'AquaTerm.framework/Headers' + File.basename(h)
      end
    end
  end

  def caveats
    <<-EOF
    Run the following commands if you would like AquaTerm residing next to other applications,
    and provide the AquaTerm framework to other applications out of Homebrew.

    sudo ln -s #{prefix+'Applications'}/AquaTerm.app /Applications/
    sudo ln -s #{prefix+'Library/Frameworks'}/AquaTerm.framework /Library/Frameworks/
    EOF
  end
end

__END__
From 2e2ea90977aed7b3b573382cacd0c2ec5f8349cf Mon Sep 17 00:00:00 2001
From: Carmine Paolino <earcar@gmail.com>
Date: Tue, 6 Apr 2010 12:29:45 +0200
Subject: [PATCH] Use native arch and SDK and -O3

---
 aquaterm/AquaTerm.xcodeproj/project.pbxproj |   89 +++++++++++++++---------------------
 1 files changed, 37 insertions(+), 52 deletions(-)

diff --git a/aquaterm/AquaTerm.xcodeproj/project.pbxproj b/aquaterm/AquaTerm.xcodeproj/project.pbxproj
index 678f3cc..cf6d389 100644
--- a/aquaterm/AquaTerm.xcodeproj/project.pbxproj
+++ b/aquaterm/AquaTerm.xcodeproj/project.pbxproj
@@ -125,9 +125,9 @@
 		CB7217FB06072ABA008DCEAD /* help.html_old */ = {isa = PBXFileReference; fileEncoding = 30; lastKnownFileType = text; name = help.html_old; path = English.lproj/help.html_old; sourceTree = SOURCE_ROOT; };
 		CB72184806072CF6008DCEAD /* ReleaseNotes */ = {isa = PBXFileReference; fileEncoding = 30; lastKnownFileType = text; path = ReleaseNotes; sourceTree = "<group>"; };
 		CB77583A056B83E300D208BA /* AQTConstants.m */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.objc; path = AQTConstants.m; sourceTree = "<group>"; };
-		CB91251407CB3BDE001D5EAF /* AquaTerm.framework-Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.xml; path = "AquaTerm.framework-Info.plist"; sourceTree = "<group>"; };
+		CB91251407CB3BDE001D5EAF /* AquaTerm.framework-Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = "AquaTerm.framework-Info.plist"; sourceTree = "<group>"; };
 		CB91259C07CB4A92001D5EAF /* AquaTerm.framework */ = {isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = AquaTerm.framework; path = build/AquaTerm.framework; sourceTree = "<group>"; };
-		CB96E43F06634622001B32F9 /* adapters.html */ = {isa = PBXFileReference; fileEncoding = 30; lastKnownFileType = file; name = adapters.html; path = ../../../../../Users/per/Documents/Source/aquaterm_help/build/adapters.html; sourceTree = SOURCE_ROOT; };
+		CB96E43F06634622001B32F9 /* adapters.html */ = {isa = PBXFileReference; fileEncoding = 30; lastKnownFileType = text.html; name = adapters.html; path = ../../../../../Users/per/Documents/Source/aquaterm_help/build/adapters.html; sourceTree = SOURCE_ROOT; };
 		CB96E44006634622001B32F9 /* releasenotes.html */ = {isa = PBXFileReference; fileEncoding = 30; lastKnownFileType = text.html; name = releasenotes.html; path = /Users/per/Documents/Source/aquaterm_help/build/releasenotes.html; sourceTree = "<absolute>"; };
 		CB9B70CC065A0AD100563010 /* English */ = {isa = PBXFileReference; lastKnownFileType = wrapper.nib; name = English; path = English.lproj/Preferences.nib; sourceTree = "<group>"; };
 		CB9B70D1065A0B9C00563010 /* AQTPrefController.h */ = {isa = PBXFileReference; fileEncoding = 30; lastKnownFileType = sourcecode.c.h; path = AQTPrefController.h; sourceTree = "<group>"; };
@@ -139,7 +139,7 @@
 		CBB800C70723A4740068A0C9 /* AQTStringDrawingAdditions.m */ = {isa = PBXFileReference; fileEncoding = 30; lastKnownFileType = sourcecode.c.objc; path = AQTStringDrawingAdditions.m; sourceTree = "<group>"; };
 		CBB8466E056C0A4B00D208BA /* AQTClientManager.h */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.h; path = AQTClientManager.h; sourceTree = "<group>"; };
 		CBB8466F056C0A4B00D208BA /* AQTClientManager.m */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.c.objc; path = AQTClientManager.m; sourceTree = "<group>"; };
-		CBC4B44A05E4C784001BE8D7 /* AquaTerm.app-Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.xml; path = "AquaTerm.app-Info.plist"; sourceTree = "<group>"; };
+		CBC4B44A05E4C784001BE8D7 /* AquaTerm.app-Info.plist */ = {isa = PBXFileReference; lastKnownFileType = text.plist.xml; path = "AquaTerm.app-Info.plist"; sourceTree = "<group>"; };
 		CBC4B44B05E4C784001BE8D7 /* AquaTerm.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = AquaTerm.app; sourceTree = BUILT_PRODUCTS_DIR; };
 		CBD51DED04EB839F00EBD329 /* CoreFoundation.framework */ = {isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = CoreFoundation.framework; path = /System/Library/Frameworks/CoreFoundation.framework; sourceTree = "<absolute>"; };
 		CBD51E0004EB84FA00EBD329 /* ApplicationServices.framework */ = {isa = PBXFileReference; lastKnownFileType = wrapper.framework; name = ApplicationServices.framework; path = /System/Library/Frameworks/ApplicationServices.framework; sourceTree = "<absolute>"; };
@@ -528,9 +528,11 @@
 		29B97313FDCFA39411CA2CEA /* Project object */ = {
 			isa = PBXProject;
 			buildConfigurationList = CB699C8C08953AAD00C4B248 /* Build configuration list for PBXProject "AquaTerm" */;
+			compatibilityVersion = "Xcode 2.4";
 			hasScannedForEncodings = 1;
 			mainGroup = 29B97314FDCFA39411CA2CEA /* AquaTerm */;
 			projectDirPath = "";
+			projectRoot = "";
 			targets = (
 				F5DB1B640219BFD2014110D6 /* Docs */,
 				CBC4B42705E4C784001BE8D7 /* AquaTerm */,
@@ -671,7 +673,6 @@
 				GCC_ENABLE_FIX_AND_CONTINUE = YES;
 				GCC_GENERATE_DEBUGGING_SYMBOLS = YES;
 				GCC_OPTIMIZATION_LEVEL = 0;
-				OPTIMIZATION_CFLAGS = "-O0";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = "";
 				OTHER_REZFLAGS = "";
@@ -740,10 +741,7 @@
 		CB699C7E08953AAD00C4B248 /* Development */ = {
 			isa = XCBuildConfiguration;
 			buildSettings = {
-				ARCHS = (
-					ppc,
-					i386,
-				);
+				ARCHS = "$(NATIVE_ARCH_ACTUAL)";
 				COPY_PHASE_STRIP = NO;
 				DYLIB_COMPATIBILITY_VERSION = 1;
 				DYLIB_CURRENT_VERSION = 1;
@@ -751,13 +749,12 @@
 				GCC_DYNAMIC_NO_PIC = NO;
 				GCC_ENABLE_FIX_AND_CONTINUE = YES;
 				GCC_GENERATE_DEBUGGING_SYMBOLS = YES;
-				GCC_OPTIMIZATION_LEVEL = 0;
+				GCC_OPTIMIZATION_LEVEL = 3;
 				GCC_PRECOMPILE_PREFIX_HEADER = YES;
 				GCC_PREFIX_HEADER = "$(SYSTEM_LIBRARY_DIR)/Frameworks/AppKit.framework/Headers/AppKit.h";
 				INFOPLIST_FILE = "AquaTerm.framework-Info.plist";
 				INSTALL_PATH = "$(LOCAL_LIBRARY_DIR)/Frameworks";
-				MACOSX_DEPLOYMENT_TARGET = 10.1;
-				OPTIMIZATION_CFLAGS = "-O0";
+				MACOSX_DEPLOYMENT_TARGET = "";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = (
 					"-framework",
@@ -767,6 +764,7 @@
 				);
 				OTHER_REZFLAGS = "";
 				PRODUCT_NAME = AquaTerm;
+				SDKROOT = "";
 				SECTORDER_FLAGS = "";
 				WARNING_CFLAGS = (
 					"-Wmost",
@@ -780,20 +778,18 @@
 		CB699C7F08953AAD00C4B248 /* Deployment */ = {
 			isa = XCBuildConfiguration;
 			buildSettings = {
-				ARCHS = (
-					ppc,
-					i386,
-				);
+				ARCHS = "$(NATIVE_ARCH_ACTUAL)";
 				COPY_PHASE_STRIP = NO;
 				DYLIB_COMPATIBILITY_VERSION = 1;
 				DYLIB_CURRENT_VERSION = 1;
 				FRAMEWORK_VERSION = A;
 				GCC_ENABLE_FIX_AND_CONTINUE = NO;
+				GCC_OPTIMIZATION_LEVEL = 3;
 				GCC_PRECOMPILE_PREFIX_HEADER = YES;
 				GCC_PREFIX_HEADER = "$(SYSTEM_LIBRARY_DIR)/Frameworks/AppKit.framework/Headers/AppKit.h";
 				INFOPLIST_FILE = "AquaTerm.framework-Info.plist";
 				INSTALL_PATH = "$(LOCAL_LIBRARY_DIR)/Frameworks";
-				MACOSX_DEPLOYMENT_TARGET = 10.1;
+				MACOSX_DEPLOYMENT_TARGET = "";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = (
 					"-framework",
@@ -803,6 +799,7 @@
 				);
 				OTHER_REZFLAGS = "";
 				PRODUCT_NAME = AquaTerm;
+				SDKROOT = "";
 				SECTORDER_FLAGS = "";
 				WARNING_CFLAGS = (
 					"-Wmost",
@@ -816,18 +813,16 @@
 		CB699C8008953AAD00C4B248 /* BuildStyle */ = {
 			isa = XCBuildConfiguration;
 			buildSettings = {
-				ARCHS = (
-					ppc,
-					i386,
-				);
+				ARCHS = "$(NATIVE_ARCH_ACTUAL)";
 				DYLIB_COMPATIBILITY_VERSION = 1;
 				DYLIB_CURRENT_VERSION = 1;
 				FRAMEWORK_VERSION = A;
+				GCC_OPTIMIZATION_LEVEL = 3;
 				GCC_PRECOMPILE_PREFIX_HEADER = YES;
 				GCC_PREFIX_HEADER = "$(SYSTEM_LIBRARY_DIR)/Frameworks/AppKit.framework/Headers/AppKit.h";
 				INFOPLIST_FILE = "AquaTerm.framework-Info.plist";
 				INSTALL_PATH = "$(LOCAL_LIBRARY_DIR)/Frameworks";
-				MACOSX_DEPLOYMENT_TARGET = 10.1;
+				MACOSX_DEPLOYMENT_TARGET = "";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = (
 					"-framework",
@@ -837,6 +832,7 @@
 				);
 				OTHER_REZFLAGS = "";
 				PRODUCT_NAME = AquaTerm;
+				SDKROOT = "";
 				SECTORDER_FLAGS = "";
 				WARNING_CFLAGS = (
 					"-Wmost",
@@ -849,18 +845,16 @@
 		CB699C8108953AAD00C4B248 /* Default */ = {
 			isa = XCBuildConfiguration;
 			buildSettings = {
-				ARCHS = (
-					ppc,
-					i386,
-				);
+				ARCHS = "$(NATIVE_ARCH_ACTUAL)";
 				DYLIB_COMPATIBILITY_VERSION = 1;
 				DYLIB_CURRENT_VERSION = 1;
 				FRAMEWORK_VERSION = A;
+				GCC_OPTIMIZATION_LEVEL = 3;
 				GCC_PRECOMPILE_PREFIX_HEADER = YES;
 				GCC_PREFIX_HEADER = "$(SYSTEM_LIBRARY_DIR)/Frameworks/AppKit.framework/Headers/AppKit.h";
 				INFOPLIST_FILE = "AquaTerm.framework-Info.plist";
 				INSTALL_PATH = "$(LOCAL_LIBRARY_DIR)/Frameworks";
-				MACOSX_DEPLOYMENT_TARGET = 10.1;
+				MACOSX_DEPLOYMENT_TARGET = "";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = (
 					"-framework",
@@ -870,6 +864,7 @@
 				);
 				OTHER_REZFLAGS = "";
 				PRODUCT_NAME = AquaTerm;
+				SDKROOT = "";
 				SECTORDER_FLAGS = "";
 				WARNING_CFLAGS = (
 					"-Wmost",
@@ -882,10 +877,7 @@
 		CB699C8308953AAD00C4B248 /* Development */ = {
 			isa = XCBuildConfiguration;
 			buildSettings = {
-				ARCHS = (
-					ppc,
-					i386,
-				);
+				ARCHS = "$(NATIVE_ARCH_ACTUAL)";
 				BUILD_VARIANTS = normal;
 				COPY_PHASE_STRIP = NO;
 				DEPLOYMENT_POSTPROCESSING = NO;
@@ -893,15 +885,14 @@
 				GCC_DYNAMIC_NO_PIC = NO;
 				GCC_ENABLE_FIX_AND_CONTINUE = YES;
 				GCC_GENERATE_DEBUGGING_SYMBOLS = YES;
-				GCC_OPTIMIZATION_LEVEL = 0;
+				GCC_OPTIMIZATION_LEVEL = 3;
 				GCC_PRECOMPILE_PREFIX_HEADER = YES;
 				GCC_PREFIX_HEADER = "$(SYSTEM_LIBRARY_DIR)/Frameworks/AppKit.framework/Headers/AppKit.h";
 				GCC_PREPROCESSOR_DEFINITIONS = "";
 				INFOPLIST_FILE = "AquaTerm.app-Info.plist";
 				INSTALL_PATH = "$(USER_APPS_DIR)";
 				LIBRARY_SEARCH_PATHS = /tmp/AquaTerm.dst/usr/local/lib;
-				MACOSX_DEPLOYMENT_TARGET = 10.1;
-				OPTIMIZATION_CFLAGS = "-O0";
+				MACOSX_DEPLOYMENT_TARGET = "";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = (
 					"-framework",
@@ -910,6 +901,7 @@
 					AppKit,
 				);
 				PRODUCT_NAME = AquaTerm;
+				SDKROOT = "";
 				SECTORDER_FLAGS = "";
 				WARNING_CFLAGS = (
 					"-Wmost",
@@ -924,23 +916,20 @@
 		CB699C8408953AAD00C4B248 /* Deployment */ = {
 			isa = XCBuildConfiguration;
 			buildSettings = {
-				ARCHS = (
-					ppc,
-					i386,
-				);
+				ARCHS = "$(NATIVE_ARCH_ACTUAL)";
 				BUILD_VARIANTS = normal;
 				COPY_PHASE_STRIP = NO;
 				DEPLOYMENT_POSTPROCESSING = NO;
 				FRAMEWORK_SEARCH_PATHS = "";
 				GCC_ENABLE_FIX_AND_CONTINUE = NO;
-				GCC_OPTIMIZATION_LEVEL = 0;
+				GCC_OPTIMIZATION_LEVEL = 3;
 				GCC_PRECOMPILE_PREFIX_HEADER = YES;
 				GCC_PREFIX_HEADER = "$(SYSTEM_LIBRARY_DIR)/Frameworks/AppKit.framework/Headers/AppKit.h";
 				GCC_PREPROCESSOR_DEFINITIONS = "";
 				INFOPLIST_FILE = "AquaTerm.app-Info.plist";
 				INSTALL_PATH = "$(USER_APPS_DIR)";
 				LIBRARY_SEARCH_PATHS = "";
-				MACOSX_DEPLOYMENT_TARGET = 10.1;
+				MACOSX_DEPLOYMENT_TARGET = "";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = (
 					"-framework",
@@ -949,6 +938,7 @@
 					AppKit,
 				);
 				PRODUCT_NAME = AquaTerm;
+				SDKROOT = "";
 				SECTORDER_FLAGS = "";
 				WARNING_CFLAGS = (
 					"-Wmost",
@@ -963,21 +953,18 @@
 		CB699C8508953AAD00C4B248 /* BuildStyle */ = {
 			isa = XCBuildConfiguration;
 			buildSettings = {
-				ARCHS = (
-					ppc,
-					i386,
-				);
+				ARCHS = "$(NATIVE_ARCH_ACTUAL)";
 				BUILD_VARIANTS = normal;
 				DEPLOYMENT_POSTPROCESSING = NO;
 				FRAMEWORK_SEARCH_PATHS = /Volumes/Ior/Source/aquaterm/build;
-				GCC_OPTIMIZATION_LEVEL = 0;
+				GCC_OPTIMIZATION_LEVEL = 3;
 				GCC_PRECOMPILE_PREFIX_HEADER = YES;
 				GCC_PREFIX_HEADER = "$(SYSTEM_LIBRARY_DIR)/Frameworks/AppKit.framework/Headers/AppKit.h";
 				GCC_PREPROCESSOR_DEFINITIONS = "";
 				INFOPLIST_FILE = "AquaTerm.app-Info.plist";
 				INSTALL_PATH = "$(USER_APPS_DIR)";
 				LIBRARY_SEARCH_PATHS = /tmp/AquaTerm.dst/usr/local/lib;
-				MACOSX_DEPLOYMENT_TARGET = 10.1;
+				MACOSX_DEPLOYMENT_TARGET = "";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = (
 					"-framework",
@@ -986,6 +973,7 @@
 					AppKit,
 				);
 				PRODUCT_NAME = AquaTerm;
+				SDKROOT = "";
 				SECTORDER_FLAGS = "";
 				WARNING_CFLAGS = (
 					"-Wmost",
@@ -999,21 +987,18 @@
 		CB699C8608953AAD00C4B248 /* Default */ = {
 			isa = XCBuildConfiguration;
 			buildSettings = {
-				ARCHS = (
-					ppc,
-					i386,
-				);
+				ARCHS = "$(NATIVE_ARCH_ACTUAL)";
 				BUILD_VARIANTS = normal;
 				DEPLOYMENT_POSTPROCESSING = NO;
 				FRAMEWORK_SEARCH_PATHS = /Volumes/Ior/Source/aquaterm/build;
-				GCC_OPTIMIZATION_LEVEL = 0;
+				GCC_OPTIMIZATION_LEVEL = 3;
 				GCC_PRECOMPILE_PREFIX_HEADER = YES;
 				GCC_PREFIX_HEADER = "$(SYSTEM_LIBRARY_DIR)/Frameworks/AppKit.framework/Headers/AppKit.h";
 				GCC_PREPROCESSOR_DEFINITIONS = "";
 				INFOPLIST_FILE = "AquaTerm.app-Info.plist";
 				INSTALL_PATH = "$(USER_APPS_DIR)";
 				LIBRARY_SEARCH_PATHS = /tmp/AquaTerm.dst/usr/local/lib;
-				MACOSX_DEPLOYMENT_TARGET = 10.1;
+				MACOSX_DEPLOYMENT_TARGET = "";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = (
 					"-framework",
@@ -1022,6 +1007,7 @@
 					AppKit,
 				);
 				PRODUCT_NAME = AquaTerm;
+				SDKROOT = "";
 				SECTORDER_FLAGS = "";
 				WARNING_CFLAGS = (
 					"-Wmost",
@@ -1040,7 +1026,6 @@
 				GCC_ENABLE_FIX_AND_CONTINUE = YES;
 				GCC_GENERATE_DEBUGGING_SYMBOLS = YES;
 				GCC_OPTIMIZATION_LEVEL = 0;
-				OPTIMIZATION_CFLAGS = "-O0";
 				OTHER_CFLAGS = "";
 				OTHER_LDFLAGS = "";
 				OTHER_REZFLAGS = "";
-- 
1.7.0.4

