# docker-image-tmpl
Docker Image Template


## [Vietnamese] Giới thiệu về cơ chế run process trong container

Docker container sử dụng cơ chế **process-based**. Người dùng có thể run docker container bằng:

- `docker run <docker-image> <command>`
- `docker run <docker-image>`

Khi thực hiện một trong hai cách trên, một docker container sẽ được tạo và thực thi **câu lệnh truyền vào** hoặc **câu lệnh mặc định** đã được định nghĩa trong docker image. Câu lệnh này sẽ sinh process có `pid = 1`. Nếu process này kết thúc thì docker container kết thúc. Tất cả các process con của `pid = 1` này sẽ bị kill.
Vấn đề được đặt ra là: **Làm sao để start, stop applications đúng cách?**

### Sử dụng entrypoint để quản lí việc start, stop application
Một kịch bản được sử dụng khi build docker image là: sử dụng `entrypoint` để thực hiện các thao tác để chuẩn bị các điều kiện, start, stop application đúng cách.

Cụ thể, nhiệm vụ của `entrypoint` là:

1. Chuẩn bị các điều kiện môi trường để start application đúng cách.
2. Start application.
3. Thực hiện các thao tác để stop application đúng cách.

**Flow sử dụng shell để làm `entrypoint`**: nhận và xử lí các command được truyền vào khi chạy docker.

1. Sử dụng python jinja2 để sinh ra các file cấu hình từ template.
File cấu hình = jinja2(file cấu hình, tham số truyền vào bằng biến `ENV`)
2. Copy file cấu hình bằng lệnh cp.
3. Thực hiện các lệnh để khởi tạo ứng dụng, chown quyền các file cần thiết. Đảm bảo ứng dụng có thể start được.
4. Chạy ứng dụng.
5. Để ứng dụng handle `SIGTERM` hoặc sử dụng shell script để handle `SIGTERM`. Đảm bảo tắt ứng dụng đúng cách.

### Tài liệu tham khảo

1. [Gracefully Stopping Docker Containers](https://labs.ctl.io/gracefully-stopping-docker-containers/)
2. [Errors and Signals and Traps Bash](http://linuxcommand.org/wss0160.php)
3. [Docker engine 1.9, Dockerfile `STOPSIGNAL`](http://docs.docker.com/engine/reference/builder/#stopsignal)


