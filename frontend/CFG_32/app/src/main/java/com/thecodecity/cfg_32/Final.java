package com.thecodecity.cfg_32;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class Final extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        System.out.println("In the page ");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.thankyou);
    }
}
