package com.knlab.web.controller;


import com.knlab.web.dto.SummaryInputDto;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.*;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
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

        HttpHeaders headers = createHeader(MediaType.APPLICATION_FORM_URLENCODED);

        MultiValueMap<String, String> requestBody = new LinkedMultiValueMap<>();
        requestBody.add("text", inputs.getText());
        requestBody.add("lang", inputs.getLanguage());

        HttpEntity request = new HttpEntity<>(requestBody, headers);

        ResponseEntity<String> response = restTemplate.exchange(SUMMARY_SERVER_URL, HttpMethod.POST,
                request, String.class);
        return response;
    }

    @PostMapping("/convert/audio")
    public ResponseEntity<String> speachToText(@RequestParam MultipartFile file) throws IOException {

        ByteArrayResource fileResource = new ByteArrayResource(file.getBytes()) {
            @Override
            public String getFilename() {
                return file.getOriginalFilename();
            }
        };

        HttpHeaders header = createHeader(MediaType.MULTIPART_FORM_DATA);
        MultiValueMap<String, Object> requestBody = new LinkedMultiValueMap<>();
        requestBody.add("file", fileResource);

        HttpEntity request = new HttpEntity<>(requestBody, header);

        ResponseEntity<String> response = restTemplate.exchange(CONVERT_SERVER_URL, HttpMethod.POST,
                request, String.class);

        return response;
    }

    private static HttpHeaders createHeader(MediaType mediaType) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(mediaType);
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        return headers;
    }

}

