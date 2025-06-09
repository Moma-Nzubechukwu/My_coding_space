#include <gtk/gtk.h>
#include <stdlib.h>

double balance = 1000.0;
GtkWidget *balance_label;
GtkWidget *amount_entry;

void update_balance_label() {
    char buf[50];
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

void login_clicked(GtkWidget *widget, gpointer data) {
    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Banking Dashboard");
    gtk_window_set_default_size(GTK_WINDOW(window), 300, 250);

    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_container_set_border_width(GTK_CONTAINER(vbox), 15);

    balance_label = gtk_label_new(NULL);
    update_balance_label();

    amount_entry = gtk_entry_new();
    gtk_entry_set_placeholder_text(GTK_ENTRY(amount_entry), "Enter amount");

    GtkWidget *deposit_btn = gtk_button_new_with_label("Deposit");
    g_signal_connect(deposit_btn, "clicked", G_CALLBACK(deposit_clicked), NULL);

    GtkWidget *withdraw_btn = gtk_button_new_with_label("Withdraw");
    g_signal_connect(withdraw_btn, "clicked", G_CALLBACK(withdraw_clicked), NULL);

    gtk_box_pack_start(GTK_BOX(vbox), balance_label, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), amount_entry, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), deposit_btn, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), withdraw_btn, FALSE, FALSE, 0);

    gtk_container_add(GTK_CONTAINER(window), vbox);
    gtk_widget_show_all(window);
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);

    GtkWidget *window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Login");
    gtk_window_set_default_size(GTK_WINDOW(window), 250, 150);

    GtkWidget *vbox = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_container_set_border_width(GTK_CONTAINER(vbox), 15);

    GtkWidget *label = gtk_label_new("Enter username:");
    GtkWidget *entry = gtk_entry_new();
    GtkWidget *btn = gtk_button_new_with_label("Login");

    g_signal_connect(btn, "clicked", G_CALLBACK(login_clicked), NULL);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    gtk_box_pack_start(GTK_BOX(vbox), label, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), entry, FALSE, FALSE, 0);
    gtk_box_pack_start(GTK_BOX(vbox), btn, FALSE, FALSE, 0);

    gtk_container_add(GTK_CONTAINER(window), vbox);
    gtk_widget_show_all(window);
    gtk_main();

    return 0;
}

