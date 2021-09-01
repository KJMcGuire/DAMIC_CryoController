#include "rpc/client.h"
#include <iostream>

int main() {
    rpc::client c("localhost", 20555);
    //float a = c.call("ReadMemVoltage").as<float>();
    //std::cout<<"Voltage: "<<a<<"\n";

    c.call("VoltageRamp",8,0,3.0,false);
    return 0;
}