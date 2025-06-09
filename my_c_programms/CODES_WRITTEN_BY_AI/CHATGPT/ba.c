#include <gtk/gtk.h>
#include <stdlib.h>

double balance = 1000.0;
GtkWidget *balance_label;
GtkWidget *amount_entry;

// Apply CSS styles
void apply_css(GtkWidget *widget) {
    GtkCssProvider *provider = gtk_css_provider_new();
    gtk_css_provider_load_from_data(provider,
        "* {"
        "  font-family: 'Segoe UI', sans-serif;"
        "  font-size: 14px;"
        "}"
        "window {"
        "  background-color: #f0f4f8;"
        "  border-radius: 10px;"
        "  padding: 10px;"
        "}"
        "entry {"
        "  background-color: #ffffff;"
        "  border: 1px solid #ccc;"
        "  border-radius: 6px;"
        "  padding: 6px;"
        "}"
        "button {"
        "  background: #4a90e2;"
        "  color: white;"
        "  border-radius: 6px;"
        "  padding: 8px 12px;"
        "}"
        "button:hover {"
        "  background: #357ab8;"
        "}"
        "label {"
        "  color: #333;"
        "}",
        -1, NULL);

    GtkStyleContext *context = gtk_widget_get_style_context(widget);
    gtk_style_context_add_provider(context,
        GTK_STYLE_PROVIDER(provider),
        GTK_STYLE_PROVIDER_PRIORITY_USER);
}

void update_balance_label() {
    char buf[64];
    snprintf(buf, sizeof(buf), "Balance: $%.2f", balance);
    gtk_label_set_text(GTK_LABEL(balance_label), buf);
}

void deposit_clicked(GtkWidget *widget, gpointer data) {
    const gchar *amount_text = gtk_entry_get_text(GTK_ENTRY(amount_entry));
    double amount = atof(amount_text);
    if (amount > 0) {
        balance += amount;
        update_balance_label();
    }
}

void withdraw_clicked(GtkWidget *widget, gpointer data) {
    const gchar *amount_text = gtk_entry_get_text(GTK_ENTRY(amount_entry));
    double amount = atof(amount_text);
    if (amount > 0 && amount <= balance) {
        balance -= amount;
        update_balance_label();
    }
}

void show_dashboard() {
    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Banking Dashboard");
    gtk_window_set_default_size(GTK_WINDOW(window), 350, 300);

    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 15);
    gtk_container_set_border_width(GTK_CONTAINER(vbox), 20);

    balance_label = gtk_label_new(NULL);
    update_balance_label();

    amount_entry = gtk_entry_new();
    gtk_entry_set_placeholder_text(GTK_ENTRY(amount_entry), "Enter amount");

    GtkWidget *deposit_btn = gtk_button_new_with_label("Deposit");
    GtkWidget *withdraw_btn = gtk_button_new_with_label("Withdraw");

    g_signal_connect(deposit_btn, "clicked", G_CALLBACK(deposit_clicked), NULL);
    g_signal_connect(withdraw_btn, "clicked", G_CALLBACK(withdraw_clicked), NULL);

    gtk_box_pack_start(GTK_BOX(vbox), balance_label, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), amount_entry, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), deposit_btn, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), withdraw_btn, FALSE, FALSE, 0);

    gtk_container_add(GTK_CONTAINER(window), vbox);

    apply_css(window);
    apply_css(vbox);
    apply_css(balance_label);
    apply_css(amount_entry);
    apply_css(deposit_btn);
    apply_css(withdraw_btn);

    gtk_widget_show_all(window);
}

void login_clicked(GtkWidget *widget, gpointer data) {
    show_dashboard();
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Login");
    gtk_window_set_default_size(GTK_WINDOW(window), 300, 180);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_container_set_border_width(GTK_CONTAINER(vbox), 20);

    GtkWidget *label = gtk_label_new("Enter username:");
    GtkWidget *entry = gtk_entry_new();
    gtk_entry_set_placeholder_text(GTK_ENTRY(entry), "Username");

    GtkWidget *btn = gtk_button_new_with_label("Login");
    g_signal_connect(btn, "clicked", G_CALLBACK(login_clicked), NULL);

    gtk_box_pack_start(GTK_BOX(vbox), label, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), entry, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), btn, FALSE, FALSE, 0);

    gtk_container_add(GTK_CONTAINER(window), vbox);

    apply_css(window);
    apply_css(vbox);
    apply_css(label);
    apply_css(entry);
    apply_css(btn);

    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}

