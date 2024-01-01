# Little_Law_LT_Predict
ML_LT_LITTLE LAW
Vì tính bảo mật của dữ liệu nên tôi đã thay đổi thông số dữ liệu nhằm tránh tiết lộ thông tin của công ty.
Vấn đề: Phòng điều độ thường hay báo sai khoảng thời gian hoàn thành đơn cho bộ phận sale từ đó gây mất lòng khách hàng và mất uy tín người bán, công ty
Giải pháp: Từ dữ liệu sẵn có, cố gắng xây dựng mô hình dự đoán thời gian hoàn thành của đơn hàng. Khoảng chênh lệch 3-4 ngày là chấp nhận được đối với kềm. 
Về hiệu suất thì model đạt được hiệu suất lần lượt như sau:
+ MSE: 12 ngày
+ std: 3.5 ngày
-> Nguyên nhân là vì quá trình điều độ của công ty có sự giao động rất lớn, nguyên tắc ít thống nhất. Lúc thì đẩy mã này lên làm trước, khi thì đẩy mã đó làm cuối từ đó có sự sai sót khiến mô hình không học được thông tin
-> Có một vài mã có số lượng dữ liệu quá ít dẫn đến làm tăng sự sai lệch cho toàn bộ mô hình
Nhìn chung về mặt ý tưởng đây là giải pháp tốt để báo trước cho khách hàng về thời gian hoàn thành đơn hàng tuy nhiên để áp dụng được cần:
+ Sự chuẩn hóa công tác của phòng điều độ. Có quy luật và thống nhất
+ Sự hỗ trợ của công ty về bổ sung thêm dữ liệu dưới chuyền sản xuất
-> Ý tưởng đã được trình bày lên xếp và đã tiến hành thử nghiệm. Vì hết thời gian thực tập nên tôi vẫn chưa hoàn thiện triển khai ở công ty.

- Hướng dẫn sử dụng:
*Input: 
VD:
<img width="565" alt="image" src="https://github.com/ThangPhanML2002/Little_Law_LT_Predict/assets/141210709/f29490a8-002f-4fdb-b400-4a0721c098d4">
<img width="577" alt="image" src="https://github.com/ThangPhanML2002/Little_Law_LT_Predict/assets/141210709/d8e18ea8-2fa3-474a-9375-d77a40e609cf">
Nhấn "Predict LT"
Kết quả:
<img width="247" alt="image" src="https://github.com/ThangPhanML2002/Little_Law_LT_Predict/assets/141210709/252c4682-865b-47d2-b1c8-3b20bd7d9527">

Chi tiết:
+ Product_code: 
-> Nhóm mã được dự báo chính xác nhất (Lệch dưới 2 ngày): D.03-14	D.04-14	D.501	D.555	D.01-14	D.01-16	D.04-16	D.05-14	D.06-14	D.06-16	D.07-14	D.09-14	D.09-16	D.18	D.205	D.206	D.302	D.401	D.506	D.507	D.507V	D.666	D.777	M.01	M.18	M.303	M.306	M.501	D.03-12	D.03-16	D.05-16	D.07-12	D.07-16	D.08-14	D.23	M.555	D.555KD	M.205	M.401

-> Nhóm mã có mức dự báo ổn (Lệch dưới 3 ngày): D.06-12	M.03	D.01-12	D.08-16	KD2-0211	D.208	C.36-12	D.09-12	D.2	KM2-0212	KM2-1176	M.04	M.23	D.05-12	C.06-12	C.04-12	C.04-14	C.112	D.08-12	D.501-14NC	KM2-1434

-> Nhóm mã có mức dự báo trung bình (Lệch trên 4 ngày): C.07-12	C.03-12	D.05V-14	M.05	CL.101C-12	KD2-0063	C.03-14	C.07-14	C.07-16	C.111	C.37-14	CL.101-12	KD2-0568	KD2-0880	KM2-0550	D.22	EVO.01V-14	CL.203-12	D.04-12	D.07-14NC	C.06-14	CL.101C-14	CL.201C-12	D.03-14NC	D.23NC	KD2-0288	D.22NC	D.501NC	KD2-1144

-> Nhóm mã có mức dự báo kém (Lệch trên 6 ngày): KD2-0007	KD2-1340	C.04-16	C.37-12	KD2-0591	KD2-0592	KD2-0595	KD2-0598	KD3-0117	KD3-0118	M.05V	N.03	N.04	N.07	C.07-3.5mm	KDT-0748	C.118	D.05V-14NC	KD2-0903	KD2-1470	KD2-1471	KD3-0926	KDT-0004	KM2-1474	CL.201C-14	KD2-0056	KD2-0064	KDT-0299	NL.102	KD2-0904	KD2-1579	KD3-1115	KD3-1578	N.118	C.05-12	D.05-12NC	D.05V-16	D.07-3.5NC	D.28NC	KD3-0372	KD3-1116	KD2-0152	KD2-1087	KD2-2-1125	C.08-16	C.36-14	C.36-16	KD2-0274	KD2-0729	KD2-0731	KD2-0732	C.01-12	C.02-12	C.05-16	C.08-12	CB.102-12	CB.202-12	EVO.01V-16	KD2-1224	KD3-0104	KD3-0287	KDT-1025	N.05	KD2-0339	KD2-1379	KD2-1380	KDT-1440	CL.201-12	CL.203-14	D.05V-12NC	KD2-0741	KD2-0742	KD2-0956	KD2-1136	KD3-0851	KD3-0927	KM2-1482	AB.202	CL.201-3.5	D.07-3.5	D.18NC	D.28	D.555NC	KD2-0048	KD2-0059	KD2-0121	KD2-0122	KD2-0125	KD2-0282	KD2-0290	KD2-0370	KD2-0371	KD2-0609	KD2-0610	KD2-0881	KD2-1341	KD2-1342	KD2-1427	KDT-0002	KDT-0003	KDT-1008	KDT-1317	KDT-1602	KM2-1475	D.03-16NC	KD2-0047	KD2-0551	KD2-0552	KD2-0701	KD2-0928	KD2-0929	KD2-0953	KD2-1000	KD2-1492	KD2-1493	KD2-1494	KD2-1495	KD2-1497	KD2-1553	KD2-1557	KD2-1558	KD3-1577	KM2-0276	KM2-1491	KMT-1560	C.05-14	C.114	C.35-14	D.03-12NC	D.05-14NC	KD2-0804	KD2-0932	KD2-0935	KD2-1580	KD2-1118	KD2-1119	KD2-1121	KD2-1122	KD2-1123	KD2-1124	KD2-1125	KDT-0673	KDT-1634	KM2-0938	C.06-16	KD2-0005	KD2-0006	KD2-0049	KD2-0050	KD2-0051	KD2-0289	KD2-1108	KD2-1479	KD2-2-1118	KD2-2-1119	KD2-2-1120	KD2-2-1121	KD2-2-1122	KD2-2-1123	KD2-2-1124	KD2-2-1126	KD2-2-1127	KD2-2-1128	KD2-2-1129	KD2-2-1130	KD2-2-1131	KD2-2-1132	KD2-2-1133	KD3-0115	KD3-0119	KD3-0120	KD3-0255	KD3-0291	KD3-0292

+ Quan_POS: Số lượng hàng cần sx. Vd cần sp 500 sp thì Quan_POS = 500
+ Month: Tháng sản xuất. VD đơn hàng bắt đầu sx vào tháng 3 thì Month = 3

*Output: 
 Chỉ cần chú ý Leadtime là bao nhiêu. 
 Các thông số bên dưới là thông số để người lập trình biết mô hình có chạy đúng không nhằm giám sát hiệu suất mô hình. Phòng cho trường hợp cần train lại model.

