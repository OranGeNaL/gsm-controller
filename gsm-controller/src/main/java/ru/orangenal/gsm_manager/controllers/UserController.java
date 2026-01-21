package ru.orangenal.gsm_manager.controllers;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
@RestController
@RequestMapping("api/v1/user")
public class UserController {
    
    @RequestMapping("me")
    public ResponseEntity<String> getUser() {
        return ResponseEntity.ok("Hello, user");
    }
}
