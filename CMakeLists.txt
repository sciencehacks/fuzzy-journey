# CMakeLists.txt
cmake_minimum_required(VERSION 3.10)

# Set the project name
project(GtkApplication)

# Find GTK3 package
find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

# Add the executable
add_executable(your_native_ui_program main.c)

# Link the executable to the GTK3 libraries
target_include_directories(your_native_ui_program PRIVATE ${GTK3_INCLUDE_DIRS})
target_link_libraries(your_native_ui_program ${GTK3_LIBRARIES})
