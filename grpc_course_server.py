# импорт библиотеки grpc
import grpc

# импорт пуля потоков для асинхронного выполнения
from concurrent import futures

# сгенерированные классы для работы с grpc-сообщениями
import course_service_pb2
# сгенерированный класс для работы с сервисом
import course_service_pb2_grpc

# реализация grpc-сервиса
class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    # реализация метода grpc-сервиса CourseService
    def GetCourse(self, request, context):
        """Метод GetCourse обрабатывает входящий запрос"""
        print(f"Получен запрос к методу GetCourse по курсу с id: {request.course_id}")
        return course_service_pb2.GetCourseResponse(course_id=f"{request.course_id}",
                                                    title=f"Автотесты API",
                                                    description=f"Будем изучать написание API-автотестов")

# функция для запуска grpc-сервера
def serve():
    # создаем сервер с использованием пула потоков (до 10 потоков)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # регистрируем сервис CourseServise на сервере
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    # настраиваем сервер для прослушивания порта 50051
    server.add_insecure_port('localhost:50051')

    # запускаем сервер
    server.start()
    print('Сервер запущен на порту 50051...')

    # ожидаем завершения работы сервера
    server.wait_for_termination()

if __name__ == "__main__":
    serve()