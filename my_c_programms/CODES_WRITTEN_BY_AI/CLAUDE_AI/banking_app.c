#include <gtk/gtk.h>
#include <stdlib.h>
#include <string.h>

#define USERNAME "user"
#define PASSWORD "pass"

GtkWidget *window, *login_grid, *bank_grid;
GtkWidget *username_entry, *password_entry;
GtkWidget *amount_entry, *balance_label;
double balance = 0.0;

void update_balance_label() {
    char buf[64];
    snprintf(buf, sizeof(buf), "Balance: $%.2f", balance);
    gtk_label_set_text(GTK_LABEL(balance_label), buf);
}

void show_error(const char *msg) {
    GtkWidget *dialog = gtk_message_dialog_new(GTK_WINDOW(window),
        GTK_DIALOG_DESTROY_WITH_PARENT,
        GTK_MESSAGE_ERROR, GTK_BUTTONS_CLOSE, "%s", msg);
    gtk_dialog_run(GTK_DIALOG(dialog));
    gtk_widget_destroy(dialog);
}

void login_clicked(GtkButton *button, gpointer user_data) {
    const char *user = gtk_entry_get_text(GTK_ENTRY(username_entry));
    const char *pass = gtk_entry_get_text(GTK_ENTRY(password_entry));

    if (strcmp(user, USERNAME) == 0 && strcmp(pass, PASSWORD) == 0) {
        gtk_widget_hide(login_grid);
        gtk_widget_show(bank_grid);
    } else {
        show_error("Invalid username or password");
    }
}

void logout_clicked(GtkButton *button, gpointer user_data) {
    gtk_entry_set_text(GTK_ENTRY(username_entry), "");
    gtk_entry_set_text(GTK_ENTRY(password_entry), "");
    gtk_entry_set_text(GTK_ENTRY(amount_entry), "");
    gtk_widget_hide(bank_grid);
    gtk_widget_show(login_grid);
}

void deposit_clicked(GtkButton *button, gpointer user_data) {
    const char *amount_str = gtk_entry_get_text(GTK_ENTRY(amount_entry));
    double amount = atof(amount_str);
    if (amount <= 0) {
        show_error("Enter a valid positive amount");
        return;
    }
    balance += amount;
    update_balance_label();
    gtk_entry_set_text(GTK_ENTRY(amount_entry), "");
}

void withdraw_clicked(GtkButton *button, gpointer user_data) {
    const char *amount_str = gtk_entry_get_text(GTK_ENTRY(amount_entry));
    double amount = atof(amount_str);
    if (amount <= 0 || amount > balance) {
        show_error("Invalid withdrawal amount");
        return;
    }
    balance -= amount;
    update_balance_label();
    gtk_entry_set_text(GTK_ENTRY(amount_entry), "");
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);
    window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(window), "Banking App");
    gtk_window_set_default_size(GTK_WINDOW(window), 300, 250);
    g_signal_connect(window, "destroy", G_CALLBACK(gtk_main_quit), NULL);

    // Login Screen
    login_grid = gtk_grid_new();
    gtk_grid_set_row_spacing(GTK_GRID(login_grid), 5);
    gtk_grid_set_column_spacing(GTK_GRID(login_grid), 5);
    gtk_container_set_border_width(GTK_CONTAINER(login_grid), 10);

    GtkWidget *login_label = gtk_label_new("Login");
    gtk_grid_attach(GTK_GRID(login_grid), login_label, 0, 0, 2, 1);

    gtk_grid_attach(GTK_GRID(login_grid), gtk_label_new("Username:"), 0, 1, 1, 1);
    username_entry = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(login_grid), username_entry, 1, 1, 1, 1);

    gtk_grid_attach(GTK_GRID(login_grid), gtk_label_new("Password:"), 0, 2, 1, 1);
    password_entry = gtk_entry_new();
    gtk_entry_set_visibility(GTK_ENTRY(password_entry), FALSE);
    gtk_grid_attach(GTK_GRID(login_grid), password_entry, 1, 2, 1, 1);

    GtkWidget *login_btn = gtk_button_new_with_label("Login");
    g_signal_connect(login_btn, "clicked", G_CALLBACK(login_clicked), NULL);
    gtk_grid_attach(GTK_GRID(login_grid), login_btn, 0, 3, 2, 1);

    // Bank Screen
    bank_grid = gtk_grid_new();
    gtk_grid_set_row_spacing(GTK_GRID(bank_grid), 5);
    gtk_grid_set_column_spacing(GTK_GRID(bank_grid), 5);
    gtk_container_set_border_width(GTK_CONTAINER(bank_grid), 10);

    balance_label = gtk_label_new("Balance: $0.00");
    gtk_grid_attach(GTK_GRID(bank_grid), balance_label, 0, 0, 2, 1);

    amount_entry = gtk_entry_new();
    gtk_grid_attach(GTK_GRID(bank_grid), amount_entry, 0, 1, 2, 1);

    GtkWidget *deposit_btn = gtk_button_new_with_label("Deposit");
    g_signal_connect(deposit_btn, "clicked", G_CALLBACK(deposit_clicked), NULL);
    gtk_grid_attach(GTK_GRID(bank_grid), deposit_btn, 0, 2, 1, 1);

    GtkWidget *withdraw_btn = gtk_button_new_with_label("Withdraw");
    g_signal_connect(withdraw_btn, "clicked", G_CALLBACK(withdraw_clicked), NULL);
    gtk_grid_attach(GTK_GRID(bank_grid), withdraw_btn, 1, 2, 1, 1);

    GtkWidget *logout_btn = gtk_button_new_with_label("Logout");
    g_signal_connect(logout_btn, "clicked", G_CALLBACK(logout_clicked), NULL);
    gtk_grid_attach(GTK_GRID(bank_grid), logout_btn, 0, 3, 2, 1);

    gtk_container_add(GTK_CONTAINER(window), login_grid);
    gtk_container_add(GTK_CONTAINER(window), bank_grid);
    gtk_widget_show_all(login_grid);
    gtk_widget_hide(bank_grid);

    gtk_widget_show(window);
    gtk_main();

    return 0;
}

