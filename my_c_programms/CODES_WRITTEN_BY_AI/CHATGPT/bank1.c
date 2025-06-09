#include <gtk/gtk.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ACCOUNTS 100
#define MAX_ACCOUNT_LEN 20
#define MAX_PIN_LEN 10

typedef struct {
    char account_num[MAX_ACCOUNT_LEN];
    char pin[MAX_PIN_LEN];
    double balance;
} Account;

typedef struct {
    GtkWidget *window;
    GtkWidget *account_entry;
    GtkWidget *pin_entry;
    GtkWidget *amount_entry;
    GtkWidget *balance_label;
    GtkWidget *login_frame;
    GtkWidget *banking_frame;
    Account accounts[MAX_ACCOUNTS];
    int account_count;
    int current_account_index;
} BankingApp;

BankingApp app;

void load_accounts() {
    FILE *file = fopen("accounts_c.txt", "r");
    app.account_count = 0;
    
    if (file) {
        while (fscanf(file, "%s %s %lf", 
                     app.accounts[app.account_count].account_num,
                     app.accounts[app.account_count].pin,
                     &app.accounts[app.account_count].balance) == 3) {
            app.account_count++;
            if (app.account_count >= MAX_ACCOUNTS) break;
        }
        fclose(file);
    }
}

void save_accounts() {
    FILE *file = fopen("accounts_c.txt", "w");
    if (file) {
        for (int i = 0; i < app.account_count; i++) {
            fprintf(file, "%s %s %.2f\n", 
                   app.accounts[i].account_num,
                   app.accounts[i].pin,
                   app.accounts[i].balance);
        }
        fclose(file);
    }
}

void show_message(const char *message, GtkMessageType type) {
    GtkWidget *dialog = gtk_message_dialog_new(GTK_WINDOW(app.window),
                                              GTK_DIALOG_DESTROY_WITH_PARENT,
                                              type,
                                              GTK_BUTTONS_OK,
                                              "%s", message);
    gtk_dialog_run(GTK_DIALOG(dialog));
    gtk_widget_destroy(dialog);
}

void update_balance_display() {
    if (app.current_account_index >= 0) {
        char balance_text[100];
        sprintf(balance_text, "Balance: $%.2f", 
                app.accounts[app.current_account_index].balance);
        gtk_label_set_text(GTK_LABEL(app.balance_label), balance_text);
    }
}

void on_create_account(GtkWidget *widget, gpointer data) {
    const char *account_num = gtk_entry_get_text(GTK_ENTRY(app.account_entry));
    const char *pin = gtk_entry_get_text(GTK_ENTRY(app.pin_entry));
    
    if (strlen(account_num) == 0 || strlen(pin) == 0) {
        show_message("Please enter account number and PIN", GTK_MESSAGE_ERROR);
        return;
    }
    
    // Check if account already exists
    for (int i = 0; i < app.account_count; i++) {
        if (strcmp(app.accounts[i].account_num, account_num) == 0) {
            show_message("Account already exists", GTK_MESSAGE_ERROR);
            return;
        }
    }
    
    if (app.account_count >= MAX_ACCOUNTS) {
        show_message("Maximum accounts reached", GTK_MESSAGE_ERROR);
        return;
    }
    
    // Create new account
    strcpy(app.accounts[app.account_count].account_num, account_num);
    strcpy(app.accounts[app.account_count].pin, pin);
    app.accounts[app.account_count].balance = 0.0;
    app.account_count++;
    
    save_accounts();
    show_message("Account created successfully!", GTK_MESSAGE_INFO);
}

void on_login(GtkWidget *widget, gpointer data) {
    const char *account_num = gtk_entry_get_text(GTK_ENTRY(app.account_entry));
    const char *pin = gtk_entry_get_text(GTK_ENTRY(app.pin_entry));
    
    if (strlen(account_num) == 0 || strlen(pin) == 0) {
        show_message("Please enter account number and PIN", GTK_MESSAGE_ERROR);
        return;
    }
    
    // Find account
    app.current_account_index = -1;
    for (int i = 0; i < app.account_count; i++) {
        if (strcmp(app.accounts[i].account_num, account_num) == 0) {
            if (strcmp(app.accounts[i].pin, pin) == 0) {
                app.current_account_index = i;
                break;
            } else {
                show_message("Invalid PIN", GTK_MESSAGE_ERROR);
                return;
            }
        }
    }
    
    if (app.current_account_index == -1) {
        show_message("Account not found", GTK_MESSAGE_ERROR);
        return;
    }
    
    // Show banking operations
    gtk_widget_hide(app.login_frame);
    gtk_widget_show(app.banking_frame);
    update_balance_display();
    show_message("Login successful!", GTK_MESSAGE_INFO);
}

void on_deposit(GtkWidget *widget, gpointer data) {
    const char *amount_text = gtk_entry_get_text(GTK_ENTRY(app.amount_entry));
    double amount = atof(amount_text);
    
    if (amount <= 0) {
        show_message("Please enter a valid positive amount", GTK_MESSAGE_ERROR);
        return;
    }
    
    app.accounts[app.current_account_index].balance += amount;
    save_accounts();
    update_balance_display();
    gtk_entry_set_text(GTK_ENTRY(app.amount_entry), "");
    
    char message[100];
    sprintf(message, "Deposited $%.2f successfully!", amount);
    show_message(message, GTK_MESSAGE_INFO);
}

void on_withdraw(GtkWidget *widget, gpointer data) {
    const char *amount_text = gtk_entry_get_text(GTK_ENTRY(app.amount_entry));
    double amount = atof(amount_text);
    
    if (amount <= 0) {
        show_message("Please enter a valid positive amount", GTK_MESSAGE_ERROR);
        return;
    }
    
    if (amount > app.accounts[app.current_account_index].balance) {
        show_message("Insufficient funds", GTK_MESSAGE_ERROR);
        return;
    }
    
    app.accounts[app.current_account_index].balance -= amount;
    save_accounts();
    update_balance_display();
    gtk_entry_set_text(GTK_ENTRY(app.amount_entry), "");
    
    char message[100];
    sprintf(message, "Withdrew $%.2f successfully!", amount);
    show_message(message, GTK_MESSAGE_INFO);
}

void on_logout(GtkWidget *widget, gpointer data) {
    gtk_widget_hide(app.banking_frame);
    gtk_widget_show(app.login_frame);
    gtk_entry_set_text(GTK_ENTRY(app.account_entry), "");
    gtk_entry_set_text(GTK_ENTRY(app.pin_entry), "");
    gtk_entry_set_text(GTK_ENTRY(app.amount_entry), "");
    app.current_account_index = -1;
}

void create_gui() {
    app.window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
    gtk_window_set_title(GTK_WINDOW(app.window), "Simple Banking App");
    gtk_window_set_default_size(GTK_WINDOW(app.window), 400, 300);
    gtk_window_set_resizable(GTK_WINDOW(app.window), FALSE);
    g_signal_connect(app.window, "destroy", G_CALLBACK(gtk_main_quit), NULL);
    
    GtkWidget *main_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_container_add(GTK_CONTAINER(app.window), main_box);
    gtk_container_set_border_width(GTK_CONTAINER(main_box), 20);
    
    // Title
    GtkWidget *title = gtk_label_new("Simple Banking System");
    gtk_widget_set_name(title, "title");
    gtk_box_pack_start(GTK_BOX(main_box), title, FALSE, FALSE, 10);
    
    // Login frame
    app.login_frame = gtk_frame_new("Login");
    gtk_box_pack_start(GTK_BOX(main_box), app.login_frame, FALSE, FALSE, 0);
    
    GtkWidget *login_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(app.login_frame), login_box);
    gtk_container_set_border_width(GTK_CONTAINER(login_box), 10);
    
    // Account entry
    GtkWidget *account_label = gtk_label_new("Account Number:");
    gtk_box_pack_start(GTK_BOX(login_box), account_label, FALSE, FALSE, 0);
    app.account_entry = gtk_entry_new();
    gtk_box_pack_start(GTK_BOX(login_box), app.account_entry, FALSE, FALSE, 0);
    
    // PIN entry
    GtkWidget *pin_label = gtk_label_new("PIN:");
    gtk_box_pack_start(GTK_BOX(login_box), pin_label, FALSE, FALSE, 0);
    app.pin_entry = gtk_entry_new();
    gtk_entry_set_visibility(GTK_ENTRY(app.pin_entry), FALSE);
    gtk_box_pack_start(GTK_BOX(login_box), app.pin_entry, FALSE, FALSE, 0);
    
    // Buttons
    GtkWidget *button_box = gtk_box_new(GTK_ORIENTATION_HORIZONTAL, 5);
    gtk_box_pack_start(GTK_BOX(login_box), button_box, FALSE, FALSE, 10);
    
    GtkWidget *login_btn = gtk_button_new_with_label("Login");
    g_signal_connect(login_btn, "clicked", G_CALLBACK(on_login), NULL);
    gtk_box_pack_start(GTK_BOX(button_box), login_btn, TRUE, TRUE, 0);
    
    GtkWidget *create_btn = gtk_button_new_with_label("Create Account");
    g_signal_connect(create_btn, "clicked", G_CALLBACK(on_create_account), NULL);
    gtk_box_pack_start(GTK_BOX(button_box), create_btn, TRUE, TRUE, 0);
    
    // Banking frame (initially hidden)
    app.banking_frame = gtk_frame_new("Banking Operations");
    gtk_box_pack_start(GTK_BOX(main_box), app.banking_frame, FALSE, FALSE, 0);
    
    GtkWidget *banking_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 5);
    gtk_container_add(GTK_CONTAINER(app.banking_frame), banking_box);
    gtk_container_set_border_width(GTK_CONTAINER(banking_box), 10);
    
    // Balance display
    app.balance_label = gtk_label_new("Balance: $0.00");
    gtk_box_pack_start(GTK_BOX(banking_box), app.balance_label, FALSE, FALSE, 10);
    
    // Amount entry
    GtkWidget *amount_label = gtk_label_new("Amount:");
    gtk_box_pack_start(GTK_BOX(banking_box), amount_label, FALSE, FALSE, 0);
    app.amount_entry = gtk_entry_new();
    gtk_box_pack_start(GTK_BOX(banking_box), app.amount_entry, FALSE, FALSE, 0);
    
    // Operation buttons
    GtkWidget *op_button_box = gtk_box_new(GTK_ORIENTATION_HORIZONTAL, 5);
    gtk_box_pack_start(GTK_BOX(banking_box), op_button_box, FALSE, FALSE, 10);
    
    GtkWidget *deposit_btn = gtk_button_new_with_label("Deposit");
    g_signal_connect(deposit_btn, "clicked", G_CALLBACK(on_deposit), NULL);
    gtk_box_pack_start(GTK_BOX(op_button_box), deposit_btn, TRUE, TRUE, 0);
    
    GtkWidget *withdraw_btn = gtk_button_new_with_label("Withdraw");
    g_signal_connect(withdraw_btn, "clicked", G_CALLBACK(on_withdraw), NULL);
    gtk_box_pack_start(GTK_BOX(op_button_box), withdraw_btn, TRUE, TRUE, 0);
    
    GtkWidget *logout_btn = gtk_button_new_with_label("Logout");
    g_signal_connect(logout_btn, "clicked", G_CALLBACK(on_logout), NULL);
    gtk_box_pack_start(GTK_BOX(banking_box), logout_btn, FALSE, FALSE, 5);
    
    // Initially hide banking frame
    gtk_widget_hide(app.banking_frame);
}

int main(int argc, char *argv[]) {
    gtk_init(&argc, &argv);
    
    load_accounts();
    app.current_account_index = -1;
    
    create_gui();
    gtk_widget_show_all(app.window);
    gtk_widget_hide(app.banking_frame);  // Hide banking operations initially
    
    gtk_main();
    
    return 0;
}
