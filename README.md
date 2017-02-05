# Description

This is a simple LSTM network, I created using tensor flow, to exploit underlying dynamics of sub events in high level actions. 
This code is a special case study used on the combined vector time series, as desribed in, our paper "Combined Static and Motion Features for Deep-Networks Based Activity Recognition in Videos", which is submitted to TCSVT (IEEE special issue). 
How ever, the code can be easily tweeked to analyize any vector time series dynamics. 

#Running the code
You can either run rnn.py or rnnHollywood.py depending on the nature of the vector time series. they both contain the same logic, But differs in the way the input data is formatted. This code will create a new time series with zero paddings.

Then this time series could be anlyzed using RNNFinal.py, after setting the paths correctly. Goodluck!
