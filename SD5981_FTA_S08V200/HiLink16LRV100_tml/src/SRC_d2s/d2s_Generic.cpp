#include <SRC_d2s/d2s_Generic.h>

#include <sstream>

#include <Common_Func/System_Common_Func.h>
#include <SRC_d2s/PatternManager.h>
#include <UserConfig.h> //TODO

INT template_selector_glb = 0;

d2s_Generic::d2s_Generic(const std::string& pName):DeviceRegisterTransactionPort(pName)
{  
	currentFormat = 0;
}

d2s_Generic::~d2s_Generic()
{
}


void d2s_Generic::setFormat(int format){
	currentFormat = format;
}


int d2s_Generic::getAddressBits(){
//    cerr << "Error in framework: getAddressBits() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);
    return 0;    
}
      
int d2s_Generic::getDataBits(){
//    cerr << "Error in framework: getDataBits() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);    
    return 0;    
}

int d2s_Generic::getHighWaveformIndex(){
//    cerr << "Error in framework: getHighWaveformIndex() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);    
    return -1;
}

int d2s_Generic::getLowWaveformIndex(){
//    cerr << "Error in framework: getLowWaveformIndex() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);
    return -1;
}
       
int d2s_Generic::getHighStrobeWaveformIndex(){
//    cerr << "Error in framework: getHighStrobeWaveformIndex() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);
    return -1;
}

int d2s_Generic::getLowStrobeWaveformIndex(){
//    cerr << "Error in framework: getLowStrobeWaveformIndex() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);
    return -1;
}
    
int d2s_Generic::getMaskStrobeWaveformIndex(){
//    cerr << "Error in framework: getMaskStrobeWaveformIndex() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);    
    return -1;
}        
  

int d2s_Generic::getPadding(){
    return 1;
}

void d2s_Generic::initWriteValueVectorMaps(){
//    cerr << "Error in framework: initWriteValueVectorMaps() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);
}


int d2s_Generic::getWriteCycles(){
	map<int, unsigned int>::const_iterator it = writeCycles.find(currentFormat);
	if(it == writeCycles.end()){
		pair<map<int, unsigned int>::const_iterator, bool> ret;
		ret = writeCycles.insert(pair<int, unsigned int> (currentFormat, PatternManager::getCyclesFromLabel(getWriteTemplatePatternName(), portName)));
		it = ret.first;
	}
    return writeCycles[currentFormat];
}


void d2s_Generic::prepareDynamicWriteLabel(long long address, long long data, const std::string& templatePatternName){
	initWriteValueVectorMaps();
    int HIGH_WFIndex = getHighWaveformIndex();
    int LOW_WFIndex = getLowWaveformIndex();
	
//    map<string, int> pinBitCount;
//    map<string, VECTOR_DATA*> pinVecData;
//
//    bitvaluePinVector::const_iterator valuesAddress = writeAddressValueVectorMap[currentFormat].begin();
//    for( ; valuesAddress != writeAddressValueVectorMap[currentFormat].end(); valuesAddress++){
//    	long long bitValue = valuesAddress->first;
//    	string pinToModify = valuesAddress->second.first;
//    	int cycle = valuesAddress->second.second;
//    	if(pinBitCount.find(pinToModify) == pinBitCount.end()){
//    		pinBitCount[pinToModify] = 0;
//    		pinVecData[pinToModify] = new VECTOR_DATA[128 * getPadding()]; //TODO: find a better way to find max bits...
//    	}
//
//    	for(int padding=0; padding<getPadding(); padding++){
//    		pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].vectorNum = cycle+padding;
//    		pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].phyWvfIndex = (address & bitValue)? HIGH_WFIndex:LOW_WFIndex;
//    	}
//    	
//    	pinBitCount[pinToModify]++;
//	}    
//    
//
//    bitvaluePinVector::const_iterator valuesData = writeDataValueVectorMap[currentFormat].begin();
//    for( ; valuesData != writeDataValueVectorMap[currentFormat].end(); valuesData++){
//    	long long bitValue = valuesData->first;
//    	string pinToModify = valuesData->second.first;
//    	int cycle = valuesData->second.second;
//
//    	if(pinBitCount.find(pinToModify) == pinBitCount.end()){
//
//    		pinBitCount[pinToModify] = 0;
//    		pinVecData[pinToModify] = new VECTOR_DATA[128 * getPadding()]; //TODO: find a better way to find max bits...
//    	}
//
//    	for(int padding=0; padding<getPadding(); padding++){
//    		pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].vectorNum = cycle+padding;
//    		pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].phyWvfIndex = (data & bitValue)? HIGH_WFIndex:LOW_WFIndex;
//    	}
//    	
//    	pinBitCount[pinToModify]++;
//	}    
//    
//        
//    map<string, int>::const_iterator pins = pinBitCount.begin();
//    for( ; pins != pinBitCount.end(); pins++)
//    {
//    	string pinToModify = pins->first;
//    	VEC_LABEL_EDIT tempVecEdit(templatePatternName, pinToModify);
//    	tempVecEdit.downloadUserVectors(pinVecData[pins->first], pins->second*getPadding());
//    	delete[] pinVecData[pinToModify];
//    }
}


void d2s_Generic::initReadValueCycleMaps(){
//	cerr << "Error in framework: initReadValueCycleMaps() needs to be overridden!" << endl;
	bool notOverridden = false;
	assert(notOverridden);
}

int d2s_Generic::getReadCycles(){
	map<int, unsigned int>::const_iterator it = readCycles.find(currentFormat);
	if(it == readCycles.end()){
		pair<map<int, unsigned int>::const_iterator, bool> ret;
		ret = readCycles.insert(pair<int, unsigned int> (currentFormat, PatternManager::getCyclesFromLabel(getReadTemplatePatternName(), portName)));
		it = ret.first;
	}
    return readCycles[currentFormat];
}


long long d2s_Generic::readFromErrorMap(int cycleOffset){
   if(!readCycleMapInitialized)  initReadValueCycleMaps();

   map<string, pair<int, int> > pinMinMaxCycles;
   map<string, map<int, unsigned long long> > pinCycleBitvalue;
   unsigned long long readValue = 0;
   
   
   for(bitvaluePinVector::const_iterator valuesData = readDataValueCycleMap[currentFormat].begin(); valuesData != readDataValueCycleMap[currentFormat].end(); valuesData++){
	   unsigned long long bitValue = valuesData->first;
	   string pin = valuesData->second.first;
	   int cycle = valuesData->second.second;

	   if(pinMinMaxCycles.find(pin) == pinMinMaxCycles.end()){
		   //first time this pin
		   pinMinMaxCycles[pin] = std::pair<int, int> (cycle, cycle);
	   }
	   else{
		   if(cycle<pinMinMaxCycles[pin].first) pinMinMaxCycles[pin].first = cycle; //min
		   if(cycle>pinMinMaxCycles[pin].second) pinMinMaxCycles[pin].second = cycle; //max
	   }
	   
	   pinCycleBitvalue[pin][cycle] = bitValue;
   }
   

   for(map<string, pair<int, int> >::const_iterator pins = pinMinMaxCycles.begin(); pins != pinMinMaxCycles.end(); pins++){
	   string pin = pins->first;
	   int minCycle = pins->second.first;
	   int maxCycle = pins->second.second;

	   long long requestedStartCycle = minCycle + cycleOffset;

//	   fwout << "ERMP? ERRM," << requestedStartCycle << "," << (maxCycle-minCycle)+1 << ",,(" << pin << ")" << endl;




	   if(hout.getLevel()&0x40){
		   //hout(GENERAL) << "ERMP? ERRM," << requestedStartCycle << "," << (maxCycle-minCycle)+1 << ",,(" << pin << ")" << endl;
	   }
	   int byteMask = 0x80;
	   //adjust start byteMask since ERMP maps to the next mod8 boundary
//	   byteMask = byteMask>>(requestedStartCycle - fwresult[0].getIntParam(1));
	   int cycle = minCycle;
//	   for(unsigned int byte=0; byte<fwresult[0][5].size(); byte++){
//		   while(byteMask>0){
//			   if(pinCycleBitvalue[pin].find(cycle) != pinCycleBitvalue[pin].end()){
//				   if(fwresult[0][5][byte]&byteMask){
//					   //bit set -->fail-->strobe for L --> so is HIGH
//					   unsigned long long bitValue = pinCycleBitvalue[pin][cycle];
//					   readValue |= bitValue;
//				   }
//				   else{
//					   //bit not set -->pass-->strobe for L --> so is LOW
//				   }
//			   }
//			   byteMask = byteMask>>1;
//			   cycle++;
//		   }
//		   byteMask = 0x80;
//	   }
   }
   
   return readValue;
}



void d2s_Generic::initReadAndExpectValueVectorMaps(){
//    cerr << "Error in framework: initReadAndExpectValueVectorMaps() needs to be overridden!" << endl;
    bool notOverridden = false;
    assert(notOverridden);
}


void d2s_Generic::prepareDynamicReadOrExpectValueLabel(long long address, const std::string& labelName, long long data, long long strobeMask){
	initReadAndExpectValueVectorMaps();
    
    int HIGH_WFIndex = getHighWaveformIndex();
    int LOW_WFIndex = getLowWaveformIndex(); 
    int highStrobeWfIndex = getHighStrobeWaveformIndex();
    int lowStrobeWfIndex = getLowStrobeWaveformIndex();
    int xStrobeWfIndex = getMaskStrobeWaveformIndex(); 
    
//    map<string, int> pinBitCount;
//    map<string, VECTOR_DATA*> pinVecData;
//
//    //address
//    bitvaluePinVector::const_iterator valuesAddress = readAndExpectAddressValueVectorMap[currentFormat].begin();
//    for( ; valuesAddress != readAndExpectAddressValueVectorMap[currentFormat].end(); valuesAddress++){
//    	long long bitValue = valuesAddress->first;
//    	string pinToModify = valuesAddress->second.first;
//    	int cycle = valuesAddress->second.second;
//    	if(pinBitCount.find(pinToModify) == pinBitCount.end()){
//    		pinBitCount[pinToModify] = 0;
//    		pinVecData[pinToModify] = new VECTOR_DATA[256 * getPadding()]; //TODO: find a better way to find max bits...
//    	}
//
//    	for(int padding=0; padding<getPadding(); padding++){
//    		pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].vectorNum = cycle+padding;
//    		pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].phyWvfIndex = (address & bitValue)? HIGH_WFIndex:LOW_WFIndex;
//    	}
//    	
//    	pinBitCount[pinToModify]++;
//	}    
//    
//    //data
//    bitvaluePinVector::const_iterator valuesData = readAndExpectDataValueVectorMap[currentFormat].begin();
//    for( ; valuesData != readAndExpectDataValueVectorMap[currentFormat].end(); valuesData++){
//    	long long bitValue = valuesData->first;
//    	string pinToModify = valuesData->second.first;
//    	int cycle = valuesData->second.second;
//    	if(pinBitCount.find(pinToModify) == pinBitCount.end()){
//    		pinBitCount[pinToModify] = 0;
//    		pinVecData[pinToModify] = new VECTOR_DATA[256 * getPadding()]; //TODO: find a better way to find max bits...
//    	}
//
//    	for(int padding=0; padding<getPadding(); padding++){
//    		pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].vectorNum = cycle+padding;
//    		if(strobeMask & bitValue){
//    			pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].phyWvfIndex = xStrobeWfIndex;
//    		}
//    		else{
//    			pinVecData[pinToModify][pinBitCount[pinToModify]*getPadding()+padding].phyWvfIndex = (data & bitValue)?highStrobeWfIndex:lowStrobeWfIndex;
//    		}
//    	}
//    	
//    	pinBitCount[pinToModify]++;
//	}       
//
//    map<string, int>::const_iterator pins = pinBitCount.begin();
//    for( ; pins != pinBitCount.end(); pins++)
//    {
//    	string pinToModify = pins->first;
//    	VEC_LABEL_EDIT tempVecEdit(labelName, pinToModify);
//    	tempVecEdit.downloadUserVectors(pinVecData[pins->first], pins->second*getPadding());
//    	delete[] pinVecData[pinToModify];
//    }
}
