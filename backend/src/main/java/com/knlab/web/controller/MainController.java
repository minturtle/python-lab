package com.knlab.web.controller;


import com.knlab.web.dto.SummaryInputDto;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.Collections;


@RestController
@RequiredArgsConstructor
public class MainController {

    private final RestTemplate restTemplate;

    @Value("${whisper.url}")
    private String CONVERT_SERVER_URL;

    @Value("${kobart.url}")
    private String SUMMARY_SERVER_URL;

    @GetMapping("/")
    public String test(){
        return "hello world!";
    }

    @PostMapping("/convert/summarization")
    public ResponseEntity<String> getSummary(@RequestBody SummaryInputDto inputs){

        if(!inputs.getLanguage().equals("ko")){
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }



        MultiValueMap<String, String> requestBody = new LinkedMultiValueMap<>();
        requestBody.add("text", inputs.getText());
        requestBody.add("lang", inputs.getLanguage());

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        HttpEntity request = new HttpEntity<>(requestBody, headers);

        ResponseEntity<String> response = restTemplate.exchange(SUMMARY_SERVER_URL, HttpMethod.POST,
                request, String.class);
        return response;
    }
}
