project(EchoApp)
cmake_minimum_required(VERSION 3.7)


add_executable(${PROJECT_NAME}_client
	src/echo_client.cpp
)
add_executable(${PROJECT_NAME}_server
	src/echo_server.cpp
)

target_link_libraries(${PROJECT_NAME}_client 
	CONAN_PKG::boost_asio
	CONAN_PKG::boost_bind
)
target_link_libraries(${PROJECT_NAME}_server 
	CONAN_PKG::boost_asio
	CONAN_PKG::boost_bind
)
target_include_directories(${PROJECT_NAME}_client
    PUBLIC 
		${PROJECT_SOURCE_DIR}/include
)

target_include_directories(${PROJECT_NAME}_server 
    PUBLIC 
		${PROJECT_SOURCE_DIR}/include
)
