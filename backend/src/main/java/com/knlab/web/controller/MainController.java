package com.knlab.web.controller;


import com.knlab.web.dto.SummaryInputDto;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;


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

    @GetMapping("/convert/summarization")
    public ResponseEntity<String> getSummary(SummaryInputDto inputs){
        if(!inputs.getLanguage().equals("ko")){
            return new ResponseEntity<>(HttpStatus.BAD_REQUEST);
        }

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);

        MultiValueMap<String, String> formBody= new LinkedMultiValueMap<>();
        formBody.add("text", inputs.getText());
        HttpEntity<MultiValueMap<String, String>> request = new HttpEntity<>(formBody, headers);
        ResponseEntity<String> response = restTemplate.postForEntity(SUMMARY_SERVER_URL, request , String.class);

        return response;
    }
}
