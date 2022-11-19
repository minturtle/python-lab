package com.knlab.web.config;


import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.http.client.BufferingClientHttpRequestFactory;
import org.springframework.http.client.SimpleClientHttpRequestFactory;
import org.springframework.http.converter.FormHttpMessageConverter;
import org.springframework.http.converter.StringHttpMessageConverter;
import org.springframework.web.client.RestTemplate;

import java.nio.charset.Charset;
import java.time.Duration;

@Configuration
public class RestTemplateConfig {

    private RestTemplateBuilder restTemplateBuilder = new RestTemplateBuilder();

    @Bean
    public RestTemplateBuilder restTemplateBuilder(){
        return restTemplateBuilder;
    }

    @Bean
    public RestTemplate restTemplate(RestTemplateBuilder restTemplateBuilder) {
        return restTemplateBuilder
                .requestFactory(() -> new BufferingClientHttpRequestFactory(new SimpleClientHttpRequestFactory()))
                .setConnectTimeout(Duration.ofMillis(180000)) // connection-timeout
                .setReadTimeout(Duration.ofMillis(180000)) // read-timeout
                .additionalMessageConverters(new StringHttpMessageConverter(Charset.forName("UTF-8")))
                .additionalMessageConverters(new FormHttpMessageConverter())
                .build();
    }
}
