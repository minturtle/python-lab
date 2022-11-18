package com.knlab.web.dto;


import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

// Summary(Kobart)를 하기위한 오리지널 텍스트를 받는 dto
@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class SummaryInputDto {
    private String text;
    private String language;
}
