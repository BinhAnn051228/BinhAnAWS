---
title: "Event 2"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
aliases:
  - /4-eventparticipated/4.2-Event2/
  - /4-eventparticipated/4.2-event2/
  - /4-EventParticipated/4.2-Event2/
  - /4-EventParticipated/4.2-event2/
---

# EVENT 2 - AWS COMMUNITY MEETUP

## AWS COMMUNITY MEETUP

### Thông tin sự kiện

| Mục | Chi tiết |
| :--- | :--- |
| **Tên sự kiện** | AWS Community Meetup |
| **Ngày tổ chức** | Thứ Bảy, ngày 15/08/2026 |
| **Thời gian** | 08:30 – 12:00 (GMT+7) |
| **Địa điểm** | Văn phòng AWS Hà Nội – Tầng 7, Grand Terra Tower, 36 Cát Linh, Đống Đa, Hà Nội |
| **Vai trò** | Người tham dự |

---

## BÁO CÁO TÓM TẮT

Các tài liệu này cung cấp một góc nhìn toàn diện, từ những bước nền tảng để làm quen với hệ sinh thái điện toán đám mây, cho đến việc đi sâu vào phân tích và thiết kế kiến trúc máy chủ để tối ưu hóa hiệu năng. Ngoài khía cạnh kỹ thuật chuyên sâu, nội dung sự kiện còn nhấn mạnh tầm quan trọng của việc xây dựng hình ảnh cá nhân và mạng lưới quan hệ chuyên nghiệp trên không gian mạng để phát triển sự nghiệp toàn diện.

### Danh sách Diễn giả

*   **Phương Nguyễn Hữu** *(Chủ đề: The Very First Step Into Cloud)*
*   **Quang Pham** - DevOps Engineer *(Chủ đề: Right Server, Right Job)*
*   **Diễn giả chuyên đề Kỹ năng mềm** *(Chủ đề: Xây dựng LinkedIn và hình ảnh chuyên nghiệp trên MXH - Personal Branding)*

---

## ĐIỂM NỔI BẬT

### Nền tảng Cloud
*   Cloud cho phép người dùng chuyển đổi chi phí đầu tư hạ tầng (CapEx) sang chi phí biến đổi và dễ dàng tiếp cận hạ tầng vật lý toàn cầu (Regions, Availability Zones) của AWS.

### Phân Tích Các Mô Hình Hosting
*   Có 5 loại hình lưu trữ chính gồm Shared Hosting, VPS, VDS, Dedicated Server, và On-Premise, đi kèm với các dịch vụ tương ứng trên AWS như Amplify, EC2 T-series, EC2 Compute-optimized và Outposts.

### Cơ Chế Ảo Hóa & Phần Cứng
*   Việc tối ưu hóa kiến trúc đòi hỏi phải hiểu rõ các giới hạn như hiện tượng "CPU steal" trên VPS, hoặc sự sụt giảm hơn 50% hiệu suất nếu RAM không được đồng bộ NUMA (NUMA-aligned) trên máy chủ VDS.

### Xây Dựng Thương Hiệu Cá Nhân
*   Kỹ sư công nghệ cần quan tâm đến "Personal Branding" và cách xây dựng một hồ sơ chuyên nghiệp trên các nền tảng mạng xã hội như LinkedIn.

---

## BÀI HỌC RÚT RA CHÍNH

### Chọn Đúng Máy Chủ Cho Từng Tác Vụ
*   Không có giải pháp lưu trữ nào là hoàn hảo cho mọi bài toán; ví dụ Shared hosting ưu tiên tiết kiệm chi phí cho các trang web nhỏ, trong khi VDS cung cấp hiệu năng CPU ổn định vì các vCPU được cấp phát độc quyền (pinned).

### Hybrid Cloud Là Một Chiến Lược Có Chủ Đích
*   Việc sử dụng Hybrid Cloud (thông qua AWS Outposts) không phải là bước lùi, mà là cấu trúc bắt buộc đối với các khối lượng công việc đòi hỏi độ trễ cực thấp hoặc bị ràng buộc bởi luật lưu trữ dữ liệu tại chỗ.

### Sức Mạnh Của Hệ Thống AWS Nitro
*   Nitro Card giúp giải phóng 100% tài nguyên CPU và bộ nhớ cho máy ảo (customer instances) bằng cách chuyển giao các tác vụ mạng, lưu trữ và bảo mật sang các thiết bị phần cứng chuyên dụng.

### Tương Tác Đám Mây Linh Hoạt
*   Người dùng có thể làm chủ và tương tác với các dịch vụ đám mây thông qua nhiều phương thức thân thiện như AWS Management Console, CLI (Command Line Interface) hoặc SDKs.

---

## TRẢI NGHIỆM SỰ KIỆN

*   Sự kiện cung cấp một lộ trình kiến thức rất cân bằng, hỗ trợ cả những người mới bắt đầu (với các định nghĩa cơ bản về IaaS, PaaS, SaaS) lẫn các kỹ sư DevOps/System dày dặn kinh nghiệm đang tìm kiếm kiến thức về bảo mật phần cứng (bare metal) và quản lý hypervisor.
*   Không chỉ tập trung vào mã nguồn hay hạ tầng, sự kiện còn mang đến không gian để các chuyên gia công nghệ trau dồi cách mở rộng cơ hội việc làm thông qua truyền thông cá nhân trên LinkedIn.

---

## BÀI HỌC KINH NGHIỆM

*   **Tính Toán Lộ Trình Nâng Cấp**: Đừng mặc định chọn các máy chủ dùng riêng đắt tiền "chỉ để phòng hờ"; thay vào đó, hãy vạch ra một lộ trình mở rộng tài nguyên linh hoạt và thiết lập mô hình tính toán tổng chi phí sở hữu (TCO) trong vòng 3 năm.
*   **Cấp Phát Tài Nguyên Vừa Đủ**: Hãy cấp phát tài nguyên đáp ứng chính xác nhu cầu hiện tại của hệ thống trước khi đưa ra các quyết định mở rộng không cần thiết nhằm tối ưu hóa chi phí.
*   **Bổ Sung Kỹ Năng Mềm Xây Dựng Hình Ảnh**: Dù kiến thức kỹ thuật có tốt đến đâu, năng lực đó cần được hiển thị và tiếp thị đúng cách thông qua hình ảnh chuyên nghiệp trên mạng xã hội.

---

## HÌNH ẢNH SỰ KIỆN

![Slide chuyên đề The Very First Step Into Cloud của diễn giả Phương Nguyễn Hữu](/images/4-eventparticipated/event2/speaker-phuong-nguyen-huu.png)

*Chuyên đề "The Very First Step Into Cloud" - Diễn giả Phương Nguyễn Hữu*

---

![Slide chuyên đề Right Server, Right Job của diễn giả Quang Pham](/images/4-eventparticipated/event2/speaker-quang-pham.png)

*Chuyên đề "Right Server, Right Job" - Diễn giả Quang Pham (DevOps Engineer)*

---

![Slide chuyên đề Xây dựng LinkedIn và hình ảnh chuyên nghiệp trên MXH - Personal Branding](/images/4-eventparticipated/event2/speaker-personal-branding.png)

*Chuyên đề "Xây dựng LinkedIn và hình ảnh chuyên nghiệp trên MXH - Personal Branding"*

---

![Toàn thể diễn giả và các bạn thành viên tham gia sự kiện AWS Community Meetup](/images/4-eventparticipated/event2/group-photo-event2.png)

*Toàn thể diễn giả và các bạn thành viên tham gia sự kiện AWS Community Meetup tại văn phòng AWS Hà Nội*
