#include <gtkmm.h>
#include <sstream>
#include <iomanip>

double balance = 1000.0;

class Dashboard : public Gtk::Window {
public:
    Dashboard() {
        set_title("Banking Dashboard");
        set_default_size(350, 300);
        set_border_width(20);

        vbox.set_spacing(15);

        update_balance_label();

        amount_entry.set_placeholder_text("Enter amount");

        deposit_button.set_label("Deposit");
        withdraw_button.set_label("Withdraw");

        deposit_button.signal_clicked().connect(sigc::mem_fun(*this, &Dashboard::on_deposit_clicked));
        withdraw_button.signal_clicked().connect(sigc::mem_fun(*this, &Dashboard::on_withdraw_clicked));

        vbox.pack_start(balance_label, Gtk::PACK_SHRINK);
        vbox.pack_start(amount_entry, Gtk::PACK_SHRINK);
        vbox.pack_start(deposit_button, Gtk::PACK_SHRINK);
        vbox.pack_start(withdraw_button, Gtk::PACK_SHRINK);

        add(vbox);

        apply_css(*this);
        show_all_children();
    }

private:
    Gtk::Box vbox{Gtk::ORIENTATION_VERTICAL};
    Gtk::Label balance_label;
    Gtk::Entry amount_entry;
    Gtk::Button deposit_button, withdraw_button;

    void update_balance_label() {
        std::ostringstream oss;
        oss << std::fixed << std::setprecision(2) << "Balance: $" << balance;
        balance_label.set_text(oss.str());
    }

    void on_deposit_clicked() {
        double amount = std::stod(amount_entry.get_text());
        if (amount > 0) {
            balance += amount;
            update_balance_label();
        }
    }

    void on_withdraw_clicked() {
        double amount = std::stod(amount_entry.get_text());
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            update_balance_label();
        }
    }

    void apply_css(Gtk::Widget& widget) {
        auto provider = Gtk::CssProvider::create();
        provider->load_from_data(
            "* { font-family: 'Segoe UI', sans-serif; font-size: 14px; }"
            "window { background-color: #f0f4f8; border-radius: 10px; padding: 10px; }"
            "entry { background: white; border: 1px solid #ccc; border-radius: 6px; padding: 6px; }"
            "button { background: #4a90e2; color: white; border-radius: 6px; padding: 8px 12px; }"
            "button:hover { background: #357ab8; }"
            "label { color: #333; }"
        );
        auto context = widget.get_style_context();
        context->add_provider(provider, GTK_STYLE_PROVIDER_PRIORITY_USER);
    }
};

class LoginWindow : public Gtk::Window {
public:
    LoginWindow() {
        set_title("Login");
        set_default_size(300, 180);
        set_border_width(20);

        vbox.set_spacing(10);
        username_entry.set_placeholder_text("Username");

        login_button.set_label("Login");
        login_button.signal_clicked().connect(sigc::mem_fun(*this, &LoginWindow::on_login_clicked));

        vbox.pack_start(label, Gtk::PACK_SHRINK);
        vbox.pack_start(username_entry, Gtk::PACK_SHRINK);
        vbox.pack_start(login_button, Gtk::PACK_SHRINK);

        label.set_text("Enter username:");
        add(vbox);

        apply_css(*this);
        show_all_children();
    }

private:
    Gtk::Box vbox{Gtk::ORIENTATION_VERTICAL};
    Gtk::Label label;
    Gtk::Entry username_entry;
    Gtk::Button login_button;

    void on_login_clicked() {
        auto dashboard = new Dashboard();
        dashboard->set_position(Gtk::WIN_POS_CENTER);
        dashboard->show();
        hide();  // hide login window
    }

    void apply_css(Gtk::Widget& widget) {
        auto provider = Gtk::CssProvider::create();
        provider->load_from_data(
            "* { font-family: 'Segoe UI', sans-serif; font-size: 14px; }"
            "window { background-color: #ffffff; border-radius: 10px; }"
            "entry { background: white; border: 1px solid #ccc; border-radius: 6px; padding: 6px; }"
            "button { background: #4a90e2; color: white; border-radius: 6px; padding: 8px 12px; }"
            "button:hover { background: #357ab8; }"
            "label { color: #333; }"
        );
        auto context = widget.get_style_context();
        context->add_provider(provider, GTK_STYLE_PROVIDER_PRIORITY_USER);
    }
};

int main(int argc, char* argv[]) {
    auto app = Gtk::Application::create(argc, argv, "org.example.banking");
    LoginWindow window;
    window.set_position(Gtk::WIN_POS_CENTER);
    return app->run(window);
}

