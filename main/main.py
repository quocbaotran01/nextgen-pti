from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox, QWidget, QListWidget, QListWidgetItem, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
from PyQt6.QtCore import QSize, Qt
import sys
import json

global_account = [
    {"name": "Trần Quốc Bảo", "account": "quocbao.tran", "password": "23042013"}
]

global_name = ''

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app_conline/Sign_in.ui", self)
        self.pushButton2_dang_ki.clicked.connect(self.show_Register)
        self.pushButton_DangNhap.clicked.connect(self.check_login)

    def show_Register(self):
        registerPage.show()
        self.close()

    def check_login(self):
        global global_name
        tai_khoan = self.lineEdit_3_tai_khoan.text()
        mat_khau = self.lineEdit_2_mat_khau.text()
        
        if not tai_khoan:
            msg_box.setText('Chưa nhập tài khoản.')
            msg_box.exec()
            return
        if not mat_khau:
            msg_box.setText('Chưa nhập mật khẩu.')
            msg_box.exec()
            return

        for account in global_account:
            if tai_khoan == account["account"] and mat_khau == account["password"]:
                global_name = account["name"]
                self.testPage = Test(global_name)
                self.testPage.show()
                self.close()
                return
        
        msg_box.setText('Sai tài khoản hoặc mật khẩu.')
        msg_box.exec()

class Register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app_conline/login.ui", self)
        self.pushButton2_dangki.clicked.connect(self.show_login)
        self.pushButton_DangKi.clicked.connect(self.check_Register)

    def show_login(self):
        loginPage.show()
        self.close()

    def check_Register(self):
        name = self.lineEdit_3_tai_khoan.text()
        account = self.lineEdit_3_tai_khoan_2.text()
        password = self.lineEdit_2_mat_khau.text()

        if not name:
            msg_box.setText('Chưa Đặt Họ Tên')
            msg_box.exec()
        elif not account:
            msg_box.setText('Chưa Đặt Tài Khoản')
            msg_box.exec()
        elif not password:
            msg_box.setText('Chưa Đặt Mật Khẩu')
            msg_box.exec()
        else:
            global global_name
            global_account.append({"name": name, "account": account, "password": password})
            global_name = name
            self.testPage = Test(global_name)
            self.testPage.show()
            self.close()

class Test(QtWidgets.QMainWindow):
    def __init__(self, name):
        super().__init__()
        uic.loadUi("app_conline/shop_cart.ui", self)
        self.data_file = "data/item_shop.json"

        self.listWidget.setViewMode(QListWidget.ViewMode.IconMode)  # Chế độ lưới
        self.listWidget.setSpacing(10)
        self.listWidget.setResizeMode(QListWidget.ResizeMode.Adjust)
        self.listWidget.setGridSize(QSize(150, 220))
        self.listWidget.setDragDropMode(QListWidget.DragDropMode.NoDragDrop)

        self.search_item_lineEdit.textChanged.connect(self.search_item)
        self.pushButton_exit.clicked.connect(self.go_back_to_login)
        self.pushButton_cart.clicked.connect(self.shop_cart)
        
        self.name_label.setText(name)

        self.load_item_json()
        self.listWidget.itemClicked.connect(self.handle_item_click)


    def load_item_json(self, keyword=""):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                products = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            products = []


        # Lọc sản phẩm theo từ khóa tìm kiếm
        filtered_products = [p for p in products if keyword.lower() in p["name"].lower()]

        self.listWidget.clear()
        for product in filtered_products:
            item_widget = self.create_product_item(product)
            item = QListWidgetItem(self.listWidget)
            item.setSizeHint(item_widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item_widget)

    def create_product_item(self, product):
        item_widget = QWidget()
        layout = QVBoxLayout()

        item_widget = QWidget()
        layout = QVBoxLayout()

        img_label = QLabel()
        image_path = product.get("image", "default.png")
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            pixmap = QPixmap("default.png")

        img_label.setPixmap(pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(img_label)

        label_text = product.get("label", "Không có nhãn")
        label = QLabel(f"<b style='color:red;'>{label_text}</b>")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        name_text = product.get("name", "Không có tên")
        name_label = QLabel(name_text)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(name_label)
        name_label.setObjectName("name_label")

        price_text = f"₫{product.get('price', 0):,}"
        price_label = QLabel(price_text)
        price_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        price_label.setStyleSheet("color: orange; font-weight: bold; font-size: 13px;")
        layout.addWidget(price_label)

        item_widget.setLayout(layout)
        return item_widget
    
    def search_item(self):
        keyword = self.search_item_lineEdit.text().strip()
        self.load_item_json(keyword)

    def go_back_to_login(self):
        loginPage.show()
        self.close()

    def handle_item_click(self, item):
        widget = self.listWidget.itemWidget(item)
        if widget:
            name_label = widget.findChild(QLabel, "name_label")
            if name_label:
                product_name = name_label.text()

                with open(self.data_file, "r", encoding="utf-8") as f:
                    products = json.load(f)
            
                for product in products:
                    if product.get("name") == product_name:
                        self.buy_page = Buy_item_page(product)
                        self.buy_page.show()
                        break
                self.close()
    
    def shop_cart(self):
        shopPage.show()
        self.close()

        

class Buy_item_page(QtWidgets.QMainWindow):
    def __init__(self, product_data):
        super().__init__()
        uic.loadUi("app_conline/buy_item_page.ui", self)
        self.spinBox_number.setMinimum(1)
        self.spinBox_number.setMaximum(1000)
        if product_data != None:
            # Gắn dữ liệu vào label
            self.name_label.setText(product_data.get("name", ""))
            self.price_label.setText(f"₫{product_data.get('price', 0):,}")
            self.label_label.setText(product_data.get("label", "Không có nhãn"))

            # Ảnh
            image_path = product_data.get("image", "default.png")
            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                pixmap = QPixmap("default.png")
            self.image_label.setPixmap(pixmap.scaled(270, 270, Qt.AspectRatioMode.KeepAspectRatio))
            
            self.pushButton_add_item.clicked.connect(lambda: self.add_item(product_data))
            self.pushButton_back.clicked.connect(lambda: self.back_page())
    def add_item(self, item):
        quantity = self.spinBox_number.value()
        try:
            with open('data/shopping_cart.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        for existing_item in data:
            if existing_item["id"] == item["id"]:
                existing_item["number_of_item"] += quantity
                break
        else:
            item_copy = item.copy()
            item_copy["number_of_item"] = quantity
            data.append(item_copy)

        with open('data/shopping_cart.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    def back_page(self):
        self.testPage = Test(global_name)
        self.testPage.show()
        self.close()

class ShopCart(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("app_conline/shopping_carter.ui", self)
        self.data_file = "data/shopping_cart.json"
        self.load_item_json()
        self.pushButton_back2.clicked.connect(self.back_page2)

    def load_item_json(self):
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                products = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            products = []

        self.listWidget.clear()
        for product in products:
            item_widget = self.create_product_item(product)
            item = QListWidgetItem(self.listWidget)
            item.setSizeHint(item_widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item_widget)

    def create_product_item(self, product):
        item_widget = QWidget()
        layout = QVBoxLayout()

        item_widget = QWidget()
        layout = QVBoxLayout()

        img_label = QLabel()
        image_path = product.get("image", "default.png")
        pixmap = QPixmap(image_path)

        if pixmap.isNull():
            pixmap = QPixmap("default.png")

        img_label.setPixmap(pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
        img_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(img_label)

        label_text = product.get("label", "Không có nhãn")
        label = QLabel(f"<b style='color:red;'>{label_text}</b>")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        name_text = product.get("name", "Không có tên")
        name_label = QLabel(name_text)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(name_label)
        name_label.setObjectName("name_label")

        price_text = f"₫{product.get('price', 0):,}"
        price_label = QLabel(price_text)
        price_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        price_label.setStyleSheet("color: orange; font-weight: bold; font-size: 13px;")
        layout.addWidget(price_label)

        number_item_text = f'Số sản phẩm: {product.get("number_of_item", 1)}'
        number_item_label = QLabel(number_item_text)
        number_item_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        number_item_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        layout.addWidget(number_item_label)
        

        item_widget.setLayout(layout)
        return item_widget
    def back_page2(self):
        self.testPage = Test(global_name)
        testPage.show()
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    registerPage = Register()
    loginPage = Login()
    testPage = Test('no name')
    buyPage = Buy_item_page(None)
    shopPage = ShopCart()
    loginPage.show()
    
    # Thiết lập hộp thoại thông báo lỗi
    msg_box = QMessageBox()
    msg_box.setWindowTitle("Lỗi")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")
    
    app.exec()
