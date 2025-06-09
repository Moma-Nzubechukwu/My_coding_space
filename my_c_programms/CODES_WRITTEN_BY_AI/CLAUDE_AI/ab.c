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
    GtkWidget *main_stack;
    GtkWidget *account_entry;
    GtkWidget *pin_entry;
    GtkWidget *amount_entry;
    GtkWidget *balance_label;
    GtkWidget *account_display_label;
    Account accounts[MAX_ACCOUNTS];
    int account_count;
    int current_account_index;
} ModernBankingApp;

ModernBankingApp app;

// CSS styling for modern look
const char *css_data = 
"window { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }"
".login-card { "
"    background: white; "
"    border-radius: 12px; "
"    box-shadow: 0 8px 32px rgba(0,0,0,0.1); "
"    padding: 32px; "
"    margin: 20px; "
"}"
".balance-card { "
"    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); "
"    border-radius: 16px; "
"    color: white; "
"    padding: 24px; "
"    margin: 16px; "
"}"
".action-card { "
"    background: white; "
"    border-radius: 12px; "
"    padding: 20px; "
"    margin: 12px; "
"    box-shadow: 0 4px 16px rgba(0,0,0,0.1); "
"}"
".title { font-size: 24px; font-weight: bold; color: #1a202c; }"
".subtitle { font-size: 14px; color: #718096; }"
".balance { font-size: 36px; font-weight: bold; }"
".modern-entry { "
"    border-radius: 8px; "
"    border: 2px solid #e2e8f0; "
"    padding: 12px; "
"    font-size: 14px; "
"}"
".modern-entry:focus { border-color: #4299e1; }"
".primary-button { "
"    background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%); "
"    border-radius: 8px; "
"    color: white; "
"    font-weight: bold; "
"    padding: 12px 24px; "
"    border: none; "
"}"
".success-button { "
"    background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); "
"    border-radius: 8px; "
"    color: white; "
"    font-weight: bold; "
"    padding: 12px 24px; "
"    border: none; "
"}"
".danger-button { "
"    background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%); "
"    border-radius: 8px; "
"    color: white; "
"    font-weight: bold; "
"    padding: 12px 24px; "
"    border: none; "
"}";

void load_accounts() {
    FILE *file = fopen("accounts_modern.txt", "r");
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
    FILE *file = fopen("accounts_modern.txt", "w");
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

void show_modern_dialog(const char *title, const char *message, const char *icon) {
    GtkWidget *dialog = gtk_message_dialog_new(GTK_WINDOW(app.window),
                                              GTK_DIALOG_MODAL,
                                              GTK_MESSAGE_INFO,
                                              GTK_BUTTONS_OK,
                                              "%s\n\n%s", icon, message);
    gtk_window_set_title(GTK_WINDOW(dialog), title);
    gtk_dialog_run(GTK_DIALOG(dialog));
    gtk_widget_destroy(dialog);
}

void update_dashboard() {
    if (app.current_account_index >= 0) {
        // Update account display
        char account_text[100];
        sprintf(account_text, "Account ••••%s", 
                app.accounts[app.current_account_index].account_num + 
                strlen(app.accounts[app.current_account_index].account_num) - 4);
        gtk_label_set_text(GTK_LABEL(app.account_display_label), account_text);
        
        // Update balance
        char balance_text[100];
        sprintf(balance_text, "$%.2f", app.accounts[app.current_account_index].balance);
        gtk_label_set_markup(GTK_LABEL(app.balance_label), 
                            g_markup_printf_escaped("<span class='balance'>%s</span>", balance_text));
    }
}

void on_create_account(GtkWidget *widget, gpointer data) {
    const char *account_num = gtk_entry_get_text(GTK_ENTRY(app.account_entry));
    const char *pin = gtk_entry_get_text(GTK_ENTRY(app.pin_entry));
    
    if (strlen(account_num) == 0 || strlen(pin) == 0) {
        show_modern_dialog("Error", "Please enter account number and PIN", "❌");
        return;
    }
    
    for (int i = 0; i < app.account_count; i++) {
        if (strcmp(app.accounts[i].account_num, account_num) == 0) {
            show_modern_dialog("Error", "Account already exists", "❌");
            return;
        }
    }
    
    if (app.account_count >= MAX_ACCOUNTS) {
        show_modern_dialog("Error", "Maximum accounts reached", "❌");
        return;
    }
    
    strcpy(app.accounts[app.account_count].account_num, account_num);
    strcpy(app.accounts[app.account_count].pin, pin);
    app.accounts[app.account_count].balance = 0.0;
    app.account_count++;
    
    save_accounts();
    show_modern_dialog("Success", "Account created successfully!", "✅");
}

void on_login(GtkWidget *widget, gpointer data) {
    const char *account_num = gtk_entry_get_text(GTK_ENTRY(app.account_entry));
    const char *pin = gtk_entry_get_text(GTK_ENTRY(app.pin_entry));
    
    if (strlen(account_num) == 0 || strlen(pin) == 0) {
        show_modern_dialog("Error", "Please enter account number and PIN", "❌");
        return;
    }
    
    app.current_account_index = -1;
    for (int i = 0; i < app.account_count; i++) {
        if (strcmp(app.accounts[i].account_num, account_num) == 0) {
            if (strcmp(app.accounts[i].pin, pin) == 0) {
                app.current_account_index = i;
                break;
            } else {
                show_modern_dialog("Error", "Invalid PIN", "❌");
                return;
            }
        }
    }
    
    if (app.current_account_index == -1) {
        show_modern_dialog("Error", "Account not found", "❌");
        return;
    }
    
    gtk_stack_set_visible_child_name(GTK_STACK(app.main_stack), "dashboard");
    update_dashboard();
    show_modern_dialog("Welcome", "Login successful!", "🎉");
}

void on_deposit(GtkWidget *widget, gpointer data) {
    const char *amount_text = gtk_entry_get_text(GTK_ENTRY(app.amount_entry));
    double amount = atof(amount_text);
    
    if (amount <= 0) {
        show_modern_dialog("Error", "Please enter a valid positive amount", "❌");
        return;
    }
    
    app.accounts[app.current_account_index].balance += amount;
    save_accounts();
    update_dashboard();
    gtk_entry_set_text(GTK_ENTRY(app.amount_entry), "");
    
    char message[100];
    sprintf(message, "Deposited $%.2f successfully!", amount);
    show_modern_dialog("Success", message, "💰");
}

void on_withdraw(GtkWidget *widget, gpointer data) {
    const char *amount_text = gtk_entry_get_text(GTK_ENTRY(app.amount_entry));
    double amount = atof(amount_text);
    
    if (amount <= 0) {
        show_modern_dialog("Error", "Please enter a valid positive amount", "❌");
        return;
    }
    
    if (amount > app.accounts[app.current_account_index].balance) {
        show_modern_dialog("Error", "Insufficient funds", "❌");
        return;
    }
    
    app.accounts[app.current_account_index].balance -= amount;
    save_accounts();
    update_dashboard();
    gtk_entry_set_text(GTK_ENTRY(app.amount_entry), "");
    
    char message[100];
    sprintf(message, "Withdrew $%.2f successfully!", amount);
    show_modern_dialog("Success", message, "💳");
}

void on_logout(GtkWidget *widget, gpointer data) {
    gtk_stack_set_visible_child_name(GTK_STACK(app.main_stack), "login");
    gtk_entry_set_text(GTK_ENTRY(app.account_entry), "");
    gtk_entry_set_text(GTK_ENTRY(app.pin_entry), "");
    gtk_entry_set_text(GTK_ENTRY(app.amount_entry), "");
    app.current_account_index = -1;
}

GtkWidget* create_login_screen() {
    GtkWidget *scroll = gtk_scrolled_window_new(NULL, NULL);
    GtkWidget *main_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 20);
    gtk_container_add(GTK_CONTAINER(scroll), main_box);
    gtk_widget_set_halign(main_box, GTK_ALIGN_CENTER);
    gtk_widget_set_valign(main_box, GTK_ALIGN_CENTER);
    
    // Bank logo and title
    GtkWidget *logo_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
    gtk_box_pack_start(GTK_BOX(main_box), logo_box, FALSE, FALSE, 0);
    
    GtkWidget *logo = gtk_label_new("🏦");
    gtk_widget_set_name(logo, "logo");
    g_object_set(logo, "margin", 20, NULL);
    gtk_box_pack_start(GTK_BOX(logo_box), logo, FALSE, FALSE, 0);
    
    GtkWidget *title = gtk_label_new("SecureBank");
    gtk_widget_set_name(title, "bank-title");
    gtk_box_pack_start(GTK_BOX(logo_box), title, FALSE, FALSE, 0);
    
    GtkWidget *subtitle = gtk_label_new("Mobile Banking");
    gtk_widget_set_name(subtitle, "bank-subtitle");
    gtk_box_pack_start(GTK_BOX(logo_box), subtitle, FALSE, FALSE, 0);
    
    // Login card
    GtkWidget *card = gtk_frame_new(NULL);
    gtk_widget_set_name(card, "login-card");
    gtk_frame_set_shadow_type(GTK_FRAME(card), GTK_SHADOW_NONE);
    gtk_box_pack_start(GTK_BOX(main_box), card, FALSE, FALSE, 0);
    
    GtkWidget *card_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 15);
    gtk_container_add(GTK_CONTAINER(card), card_box);
    gtk_container_set_border_width(GTK_CONTAINER(card_box), 30);
    
    // Welcome text
    GtkWidget *welcome = gtk_label_new("Welcome Back");
    gtk_widget_set_name(welcome, "welcome-title");
    gtk_box_pack_start(GTK_BOX(card_box), welcome, FALSE, FALSE, 0);
    
    GtkWidget *desc = gtk_label_new("Sign in to your account");
    gtk_widget_set_name(desc, "welcome-desc");
    gtk_box_pack_start(GTK_BOX(card_box), desc, FALSE, FALSE, 0);
    
    // Form fields
    GtkWidget *account_label = gtk_label_new("Account Number");
    gtk_widget_set_halign(account_label, GTK_ALIGN_START);
    gtk_box_pack_start(GTK_BOX(card_box), account_label, FALSE, FALSE, 0);
    
    app.account_entry = gtk_entry_new();
    gtk_widget_set_name(app.account_entry, "modern-entry");
    gtk_entry_set_placeholder_text(GTK_ENTRY(app.account_entry), "Enter your account number");
    gtk_box_pack_start(GTK_BOX(card_box), app.account_entry, FALSE, FALSE, 0);
    
    GtkWidget *pin_label = gtk_label_new("PIN");
    gtk_widget_set_halign(pin_label, GTK_ALIGN_START);
    gtk_box_pack_start(GTK_BOX(card_box), pin_label, FALSE, FALSE, 0);
    
    app.pin_entry = gtk_entry_new();
    gtk_widget_set_name(app.pin_entry, "modern-entry");
    gtk_entry_set_visibility(GTK_ENTRY(app.pin_entry), FALSE);
    gtk_entry_set_placeholder_text(GTK_ENTRY(app.pin_entry), "Enter your PIN");
    gtk_box_pack_start(GTK_BOX(card_box), app.pin_entry, FALSE, FALSE, 0);
   
   // Login button
   GtkWidget *login_btn = gtk_button_new_with_label("Sign In");
   gtk_widget_set_name(login_btn, "primary-button");
   g_signal_connect(login_btn, "clicked", G_CALLBACK(on_login), NULL);
   gtk_box_pack_start(GTK_BOX(card_box), login_btn, FALSE, FALSE, 0);
   
   // Create account button
   GtkWidget *create_btn = gtk_button_new_with_label("Create New Account");
   gtk_widget_set_name(create_btn, "secondary-button");
   g_signal_connect(create_btn, "clicked", G_CALLBACK(on_create_account), NULL);
   gtk_box_pack_start(GTK_BOX(card_box), create_btn, FALSE, FALSE, 0);
   
   return scroll;
}

GtkWidget* create_dashboard_screen() {
   GtkWidget *scroll = gtk_scrolled_window_new(NULL, NULL);
   GtkWidget *main_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 0);
   gtk_container_add(GTK_CONTAINER(scroll), main_box);
   
   // Header
   GtkWidget *header = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
   gtk_widget_set_name(header, "header");
   gtk_box_pack_start(GTK_BOX(main_box), header, FALSE, FALSE, 0);
   g_object_set(header, "margin", 20, NULL);
   
   GtkWidget *greeting = gtk_label_new("Good Morning");
   gtk_widget_set_name(greeting, "greeting");
   gtk_widget_set_halign(greeting, GTK_ALIGN_START);
   gtk_box_pack_start(GTK_BOX(header), greeting, FALSE, FALSE, 0);
   
   app.account_display_label = gtk_label_new("Account ••••0000");
   gtk_widget_set_name(app.account_display_label, "account-info");
   gtk_widget_set_halign(app.account_display_label, GTK_ALIGN_START);
   gtk_box_pack_start(GTK_BOX(header), app.account_display_label, FALSE, FALSE, 0);
   
   // Balance card
   GtkWidget *balance_card = gtk_frame_new(NULL);
   gtk_widget_set_name(balance_card, "balance-card");
   gtk_frame_set_shadow_type(GTK_FRAME(balance_card), GTK_SHADOW_NONE);
   gtk_box_pack_start(GTK_BOX(main_box), balance_card, FALSE, FALSE, 0);
   
   GtkWidget *balance_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
   gtk_container_add(GTK_CONTAINER(balance_card), balance_box);
   gtk_container_set_border_width(GTK_CONTAINER(balance_box), 25);
   
   GtkWidget *balance_title = gtk_label_new("Available Balance");
   gtk_widget_set_name(balance_title, "balance-title");
   gtk_widget_set_halign(balance_title, GTK_ALIGN_START);
   gtk_box_pack_start(GTK_BOX(balance_box), balance_title, FALSE, FALSE, 0);
   
   app.balance_label = gtk_label_new("$0.00");
   gtk_widget_set_name(app.balance_label, "balance-amount");
   gtk_widget_set_halign(app.balance_label, GTK_ALIGN_START);
   gtk_box_pack_start(GTK_BOX(balance_box), app.balance_label, FALSE, FALSE, 0);
   
   // Quick actions card
   GtkWidget *actions_card = gtk_frame_new(NULL);
   gtk_widget_set_name(actions_card, "action-card");
   gtk_frame_set_shadow_type(GTK_FRAME(actions_card), GTK_SHADOW_NONE);
   gtk_box_pack_start(GTK_BOX(main_box), actions_card, FALSE, FALSE, 0);
   
   GtkWidget *actions_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 15);
   gtk_container_add(GTK_CONTAINER(actions_card), actions_box);
   gtk_container_set_border_width(GTK_CONTAINER(actions_box), 20);
   
   GtkWidget *actions_title = gtk_label_new("Quick Actions");
   gtk_widget_set_name(actions_title, "section-title");
   gtk_widget_set_halign(actions_title, GTK_ALIGN_START);
   gtk_box_pack_start(GTK_BOX(actions_box), actions_title, FALSE, FALSE, 0);
   
   // Amount input
   GtkWidget *amount_label = gtk_label_new("Amount");
   gtk_widget_set_halign(amount_label, GTK_ALIGN_START);
   gtk_box_pack_start(GTK_BOX(actions_box), amount_label, FALSE, FALSE, 0);
   
   app.amount_entry = gtk_entry_new();
   gtk_widget_set_name(app.amount_entry, "modern-entry");
   gtk_entry_set_placeholder_text(GTK_ENTRY(app.amount_entry), "$0.00");
   gtk_box_pack_start(GTK_BOX(actions_box), app.amount_entry, FALSE, FALSE, 0);
   
   // Action buttons
   GtkWidget *button_box = gtk_box_new(GTK_ORIENTATION_HORIZONTAL, 10);
   gtk_box_pack_start(GTK_BOX(actions_box), button_box, FALSE, FALSE, 0);
   
   GtkWidget *deposit_btn = gtk_button_new_with_label("💰 Deposit");
   gtk_widget_set_name(deposit_btn, "success-button");
   g_signal_connect(deposit_btn, "clicked", G_CALLBACK(on_deposit), NULL);
   gtk_box_pack_start(GTK_BOX(button_box), deposit_btn, TRUE, TRUE, 0);
   
   GtkWidget *withdraw_btn = gtk_button_new_with_label("💳 Withdraw");
   gtk_widget_set_name(withdraw_btn, "danger-button");
   g_signal_connect(withdraw_btn, "clicked", G_CALLBACK(on_withdraw), NULL);
   gtk_box_pack_start(GTK_BOX(button_box), withdraw_btn, TRUE, TRUE, 0);
   
   // Recent transactions (placeholder)
   GtkWidget *transactions_card = gtk_frame_new(NULL);
   gtk_widget_set_name(transactions_card, "action-card");
   gtk_frame_set_shadow_type(GTK_FRAME(transactions_card), GTK_SHADOW_NONE);
   gtk_box_pack_start(GTK_BOX(main_box), transactions_card, FALSE, FALSE, 0);
   
   GtkWidget *trans_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 10);
   gtk_container_add(GTK_CONTAINER(transactions_card), trans_box);
   gtk_container_set_border_width(GTK_CONTAINER(trans_box), 20);
   
   GtkWidget *trans_title = gtk_label_new("Recent Transactions");
   gtk_widget_set_name(trans_title, "section-title");
   gtk_widget_set_halign(trans_title, GTK_ALIGN_START);
   gtk_box_pack_start(GTK_BOX(trans_box), trans_title, FALSE, FALSE, 0);
   
   GtkWidget *no_trans = gtk_label_new("No recent transactions");
   gtk_widget_set_name(no_trans, "placeholder-text");
   gtk_box_pack_start(GTK_BOX(trans_box), no_trans, FALSE, FALSE, 0);
   
   // Logout button
   GtkWidget *logout_card = gtk_frame_new(NULL);
   gtk_widget_set_name(logout_card, "action-card");
   gtk_frame_set_shadow_type(GTK_FRAME(logout_card), GTK_SHADOW_NONE);
   gtk_box_pack_start(GTK_BOX(main_box), logout_card, FALSE, FALSE, 0);
   
   GtkWidget *logout_box = gtk_box_new(GTK_ORIENTATION_VERTICAL, 0);
   gtk_container_add(GTK_CONTAINER(logout_card), logout_box);
   gtk_container_set_border_width(GTK_CONTAINER(logout_box), 20);
   
   GtkWidget *logout_btn = gtk_button_new_with_label("Sign Out");
   gtk_widget_set_name(logout_btn, "secondary-button");
   g_signal_connect(logout_btn, "clicked", G_CALLBACK(on_logout), NULL);
   gtk_box_pack_start(GTK_BOX(logout_box), logout_btn, FALSE, FALSE, 0);
   
   return scroll;
}

void apply_css() {
   GtkCssProvider *provider = gtk_css_provider_new();
   
   // Enhanced CSS with more modern styling
   const char *enhanced_css = 
   "window { "
   "    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); "
   "    font-family: 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif; "
   "}"
   "#login-card, #action-card { "
   "    background: rgba(255, 255, 255, 0.95); "
   "    border-radius: 16px; "
   "    box-shadow: 0 20px 40px rgba(0,0,0,0.1); "
   "    margin: 16px; "
   "}"
   "#balance-card { "
   "    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); "
   "    border-radius: 20px; "
   "    color: white; "
   "    margin: 16px; "
   "    box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3); "
   "}"
   "#logo { font-size: 48px; }"
   "#bank-title { "
   "    font-size: 28px; "
   "    font-weight: bold; "
   "    color: white; "
   "}"
   "#bank-subtitle { "
   "    font-size: 16px; "
   "    color: rgba(255, 255, 255, 0.8); "
   "}"
   "#welcome-title { "
   "    font-size: 24px; "
   "    font-weight: bold; "
   "    color: #1a202c; "
   "}"
   "#welcome-desc { "
   "    font-size: 14px; "
   "    color: #718096; "
   "}"
   "#greeting { "
   "    font-size: 18px; "
   "    font-weight: bold; "
   "    color: white; "
   "}"
   "#account-info { "
   "    font-size: 14px; "
   "    color: rgba(255, 255, 255, 0.8); "
   "}"
   "#balance-title { "
   "    font-size: 14px; "
   "    color: rgba(255, 255, 255, 0.9); "
   "}"
   "#balance-amount { "
   "    font-size: 36px; "
   "    font-weight: bold; "
   "    color: white; "
   "}"
   "#section-title { "
   "    font-size: 18px; "
   "    font-weight: bold; "
   "    color: #2d3748; "
   "}"
   "#modern-entry { "
   "    border-radius: 12px; "
   "    border: 2px solid #e2e8f0; "
   "    padding: 14px; "
   "    font-size: 16px; "
   "    background: #f7fafc; "
   "}"
   "#modern-entry:focus { "
   "    border-color: #4299e1; "
   "    background: white; "
   "}"
   "#primary-button { "
   "    background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%); "
   "    border-radius: 12px; "
   "    color: white; "
   "    font-weight: bold; "
   "    padding: 16px; "
   "    border: none; "
   "    font-size: 16px; "
   "}"
   "#secondary-button { "
   "    background: transparent; "
   "    border: 2px solid #e2e8f0; "
   "    border-radius: 12px; "
   "    color: #4a5568; "
   "    padding: 14px; "
   "    font-size: 14px; "
   "}"
   "#success-button { "
   "    background: linear-gradient(135deg, #48bb78 0%, #38a169 100%); "
   "    border-radius: 12px; "
   "    color: white; "
   "    font-weight: bold; "
   "    padding: 16px; "
   "    border: none; "
   "    font-size: 14px; "
   "}"
   "#danger-button { "
   "    background: linear-gradient(135deg, #f56565 0%, #e53e3e 100%); "
   "    border-radius: 12px; "
   "    color: white; "
   "    font-weight: bold; "
   "    padding: 16px; "
   "    border: none; "
   "    font-size: 14px; "
   "}"
   "#placeholder-text { "
   "    color: #a0aec0; "
   "    font-style: italic; "
   "}";
   
   gtk_css_provider_load_from_data(provider, enhanced_css, -1, NULL);
   gtk_style_context_add_provider_for_screen(gdk_screen_get_default(),
                                            GTK_STYLE_PROVIDER(provider),
                                            GTK_STYLE_PROVIDER_PRIORITY_APPLICATION);
   g_object_unref(provider);
}

void create_modern_gui() {
   app.window = gtk_window_new(GTK_WINDOW_TOPLEVEL);
   gtk_window_set_title(GTK_WINDOW(app.window), "SecureBank Mobile");
   gtk_window_set_default_size(GTK_WINDOW(app.window), 375, 667);
   gtk_window_set_resizable(GTK_WINDOW(app.window), FALSE);
   g_signal_connect(app.window, "destroy", G_CALLBACK(gtk_main_quit), NULL);
   
   // Apply modern styling
   apply_css();
   
   // Create stack for navigation
   app.main_stack = gtk_stack_new();
   gtk_container_add(GTK_CONTAINER(app.window), app.main_stack);
   
   // Add screens to stack
   GtkWidget *login_screen = create_login_screen();
   gtk_stack_add_named(GTK_STACK(app.main_stack), login_screen, "login");
   
   GtkWidget *dashboard_screen = create_dashboard_screen();
   gtk_stack_add_named(GTK_STACK(app.main_stack), dashboard_screen, "dashboard");
   
   // Start with login screen
   gtk_stack_set_visible_child_name(GTK_STACK(app.main_stack), "login");
}

int main(int argc, char *argv[]) {
   gtk_init(&argc, &argv);
   
   load_accounts();
   app.current_account_index = -1;
   
   create_modern_gui();
   gtk_widget_show_all(app.window);
   
   gtk_main();
   
   return 0;
}
