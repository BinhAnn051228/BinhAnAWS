---
title: "Chia sẻ, đóng góp ý kiến"
date: 2026-07-14
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

Trải qua kỳ thực tập **Workforce Bootcamp - First Cloud AI Journey** đầy ý nghĩa tại **AWS Việt Nam**, với tư cách là một sinh viên chuyên ngành **Mạng máy tính và truyền thông dữ liệu** thuộc **Trường Đại học Xây Dựng Hà Nội**, tôi xin chia sẻ những góc nhìn, trải nghiệm thực tế và đóng góp ý kiến nhằm hoàn thiện chương trình cho các khóa tiếp theo:

### Đánh giá chung về chương trình

**1. Môi trường học tập và làm việc**  
Chương trình được thiết kế rất khoa học và thực tế. Các bài giảng kết hợp chặt chẽ với hệ thống bài lab thực hành, giúp thực tập sinh không chỉ nắm chắc lý thuyết dịch vụ đám mây AWS mà còn có cơ hội áp dụng trực tiếp vào dự án lớn (**FCAJ AWS DevSecOps Pipeline Workshop**). Lộ trình theo dõi tiến độ rõ ràng giúp sinh viên chủ động quản lý thời gian và nâng cao tính tự giác.

**2. Sự hỗ trợ từ Mentor & Đội ngũ Admin**  
Đội ngũ Mentor sở hữu chuyên môn sâu rộng và phong cách hướng dẫn tận tâm. Trong quá trình triển khai các cấu hình phức tạp (như phân quyền IAM đặc quyền tối thiểu, thiết lập 4 cổng bảo mật CodeBuild, hay xử lý xung đột state lock trong Terraform), các Mentor luôn định hướng phương pháp phân tích log (CloudWatch Logs) và tư duy gỡ lỗi (troubleshooting) từ gốc rễ thay vì cung cấp ngay giải pháp sẵn có. Ban Admin cũng hỗ trợ kỹ thuật và môi trường thực hành AWS rất kịp thời.

**3. Sự phù hợp với chuyên ngành Mạng máy tính & Truyền thông dữ liệu**  
Là sinh viên ngành **Mạng máy tính và truyền thông dữ liệu**, tôi nhận thấy dự án thực tập có sự gắn kết vô cùng chặt chẽ với ngành học:
*   Vận dụng trực tiếp các kiến thức nền tảng về định tuyến (Routing), phân vùng mạng con (Subnetting) và cổng mạng (Internet Gateway) vào việc thiết kế kiến trúc **Amazon VPC**.
*   Hiểu rõ cơ chế kiểm soát gói tin và an ninh mạng thông qua **Security Groups** và **Network ACLs**, đặc biệt là quy chuẩn đóng hoàn toàn cổng quản trị SSH (port 22) ra Internet và thay thế bằng **AWS Systems Manager (SSM) Session Manager**.
*   Trải nghiệm thực tế cách tự động hóa hạ tầng mạng bằng mã (**Terraform IaC**) và thiết lập các chốt chặn an ninh Shift-Left (**Checkov, Gitleaks, Bandit, Trivy**) trong quy trình phân phối phần mềm liên tục.

**4. Cơ hội học hỏi & Phát triển kỹ năng**  
Kỳ thực tập đã giúp tôi phát triển toàn diện cả về kỹ năng cứng lẫn kỹ năng mềm: từ việc làm chủ quy trình CI/CD tự động với AWS CodePipeline, tư duy bảo mật Shift-Left trong chuỗi cung ứng phần mềm, cho đến kỹ năng viết tài liệu kỹ thuật chuẩn mực và quản lý công việc theo mốc thời gian.

**5. Văn hóa & Tinh thần cộng đồng**  
Văn hóa chia sẻ cởi mở tại **AWS Study Group** và cộng đồng **First Cloud Journey (FCAJ)** là nguồn động lực rất lớn. Việc tham gia các sự kiện thực tế như **AWS Vietnam Community Meetup** tại văn phòng AWS Hà Nội giúp tôi mở rộng tầm nhìn về xu hướng công nghệ (AI Agents, Cloud Infrastructure) và xây dựng mạng lưới quan hệ nghề nghiệp quý báu.

---

### Trả lời câu hỏi khảo sát

*   **Điều bạn hài lòng nhất trong thời gian thực tập?**  
    Đó là việc được tự tay thiết kế và vận hành hoàn chỉnh một hệ sinh thái DevSecOps tự động hóa 100% trên AWS: từ khâu push code trên GitHub, tự động quét phát hiện lỗ hổng qua 4 security gates, tạo bản kế hoạch thay đổi hạ tầng có cổng phê duyệt (Manual Approval), đến tự động triển khai và chạy smoke test xác thực thành công trên máy chủ EC2.
*   **Điều bạn nghĩ chương trình cần cải thiện cho các khóa sau?**  
    Có thể bổ sung thêm các buổi trao đổi kỹ thuật nhóm nhỏ (Tech Sharing Check-in) giữa các thực tập sinh để cùng nhau thảo luận các lỗi thường gặp trong quá trình làm việc với Terraform và CodePipeline.
*   **Bạn có khuyên bạn bè tham gia chương trình này không?**  
    Chắc chắn có. Đây là một chương trình đào tạo thực chiến xuất sắc, là cầu nối vững chắc giúp sinh viên ngành mạng và công nghệ thông tin tự tin bước vào môi trường doanh nghiệp điện toán đám mây.

---

### Đề xuất & Mong muốn

*   **Đề xuất**: Ban tổ chức có thể mở rộng thêm một số chuyên đề nâng cao về kiến trúc mạng đám mây phân tán (Transit Gateway, VPC Peering, Hybrid Cloud qua AWS Outposts) và tích hợp các công cụ quan sát chuyên sâu (AWS X-Ray, CloudWatch Container Insights) cho các dự án sau.
*   **Mong muốn**: Tiếp tục đồng hành, tích cực tham gia các buổi sinh hoạt chuyên môn của cộng đồng AWS Việt Nam và chia sẻ lại kinh nghiệm cho các bạn sinh viên khóa sau.