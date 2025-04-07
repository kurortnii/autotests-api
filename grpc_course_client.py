import grpc

import course_service_pb2
import course_service_pb2_grpc

# устанавливаем соединения с сервером
channel = grpc.insecure_channel('localhost:50051')
stub = course_service_pb2_grpc.CourseServiceStub(channel)

# отправляем запрос
response = stub.GetCourse(course_service_pb2.GetCourseRequest(course_id="api-course"))
print(response)