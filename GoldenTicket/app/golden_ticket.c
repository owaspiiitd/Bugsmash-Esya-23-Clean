#include <stdio.h>

char* doc=
    "Welcome to the ticket stand!\n"
    "Your current balance is 10000.\n"
    "You currently have 0 tickets.\n"
    "A single regular ticket costs 1000.\n"
    "The golden ticket costs 1000000 regular tickets.\n";

char* step=
    "Enter 0 to buy regular tickets.\n"
    "Enter 1 to buy the golden ticket.\n"
    "Enter 2 to exit.\n"
    "\nYour choice: "; 

char* buy=
    "How many regular tickets would you like to buy? ";

char* succ=
    "You bought the golden ticket!\n";

char* fail=
    "You didn't buy the golden ticket.\n";

#define FALSE 0
#define TRUE 1

int main(){

    int balance = 10000;
    int opt;
    int cnt;
    int price = 1000000;
    int tickets = 0;
    int bought = FALSE;

    printf("%s\n", doc);

    do{

        printf("%s", step);
        scanf("%d", &opt);

        if(opt == 0){
            printf("%s", buy);
            scanf("%d", &cnt);
            if(balance - cnt*1000 >= 0){
                balance = balance - cnt*1000;
                tickets += cnt;
                printf("You bought %d tickets. Your balance is now %d and you have %d tickets.\n\n", cnt, balance, tickets);
            }else{
                printf("Not enough balance.\n\n");
            }
        }else if(opt == 1){
            if(tickets >= price){
                bought = TRUE;
                opt = 2;
            }else{
                printf("Not enough tickets.\n\n");
            }
        }
    }while(opt != 2);

    printf("%s\n", bought ? succ : fail);

}
