package main

import (
	"fmt"
)

func main() {
	credential_map := map[string]string{
		"user1": "pass1",
		"user2": "pass2",
		"user3": "pass3",
	}
	var username_input string
	var password_input string
	fmt.Println("Please enter the username")
	fmt.Scanln(&username_input)
	if value, ok := credential_map[username_input]; ok{
		fmt.Println("Please enter the password")
		fmt.Scanln(&password_input)
		if password_input == value{
			fmt.Println("Login successful")
			return
		} else{
			fmt.Println("Password Incorrect")
			return
		}
	}
	fmt.Println("Username not found")
}
