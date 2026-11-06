# Phúc Nguyễn Media - hướng dẫn cập nhật trang

Sau khi bấm **Commit**, đợi khoảng 1-2 phút, trang tự cập nhật.

## Thêm ảnh vào album có sẵn
Vào thư mục `albums/<tên album>` > **Add file > Upload files** > kéo ảnh vào > **Commit changes**.

## Tạo album mới
**Add file > Create new file**, gõ tên: `albums/Tên album mới/ghi-chu.txt` (gõ dấu / để tạo thư mục), Commit. Sau đó upload ảnh vào thư mục đó.
Tên thư mục chính là tên album. Thêm số ở đầu để sắp xếp, ví dụ `3. Đám cưới Minh & Lan` (số sẽ không hiện trên trang). Ảnh đầu tiên là ảnh bìa.

## Album lấy ảnh từ NAS (không tải ảnh gốc lên web)
Chuẩn bị: tạo link chia sẻ công khai cho album trên NAS (Synology Photos: Chia sẻ > Tạo link; QNAP: Chia sẻ link).
1. Vào `albums/<tên album>/` > **Add file > Upload files**, chỉ tải **1 ảnh bìa** (nhẹ, dưới 300 KB). Đặt tên ảnh bắt đầu bằng `bia` (ví dụ `bia.jpg`) để làm ảnh bìa.
2. Trong cùng thư mục, **Add file > Create new file**, đặt tên `albums/<tên album>/link.txt`, dán link NAS vào dòng đầu, **Commit changes**.
3. Đợi 1-2 phút. Khách bấm vào album sẽ mở link NAS ở tab mới.

Album không có `link.txt` vẫn hoạt động như cũ (xem ảnh ngay trên trang). Để đổi link: sửa `link.txt`. Để bỏ link NAS: xóa `link.txt`.

## Đổi ảnh lớn ở đầu trang
Thư mục `hero/`: ảnh sắp xếp theo tên (1.jpg, 2.jpg...). Thay hoặc thêm ảnh rồi Commit.

## Thêm / xoá video
Mở file `videos.txt` (bấm biểu tượng bút chì), thêm một dòng: `link YouTube | Tên video`, rồi Commit.

## Lưu ý
- Ảnh nên là .jpg / .png / .webp, mỗi ảnh dưới 1-2 MB cho trang tải nhanh.
- Không sửa file `media.js` bằng tay, nó tự tạo lại mỗi lần bạn Commit.
