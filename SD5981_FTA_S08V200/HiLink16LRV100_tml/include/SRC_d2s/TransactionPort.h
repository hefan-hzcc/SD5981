#ifndef TRANSACTIONPORT_H_
#define TRANSACTIONPORT_H_

#include <string>
#include <vector>
#include <map>

#include <SRC_d2s/d2s_status.h>
#include <SRC_d2s/d2sModes.h>
#include <SRC_d2s/md5_pack.h>

class d2sFramework;

class TransactionPort
{
public:
	TransactionPort(const std::string& portName);
	virtual ~TransactionPort();
    virtual std::string getPortName();
    
    virtual void setFrameworkMode(const d2sFrameWorkModeType::Enum mode);
    virtual void preExec(const std::string& burstName);
    virtual void postExec(const std::string& executedId, bool executionWasSuccessful);
    
    virtual void execLabel(const std::string& labelName, unsigned long long cycles=0,bool check_cycle=true);
    virtual void enablePassFailCheckForNextExecution();
    virtual bool hasPassed(const std::string& burst_id);
    virtual void hasPassed(const std::string& id,bool& isAllSitesPassed,bool& isAllSitesFailed);
 //   virtual void hasPassed(const std::string& id,bool& isAllSitesPassed,bool& isAllSitesFailed,ARRAY_I& eachSiteResult);
    virtual bool hasAllSitesPassed(const std::string& id);
    virtual bool hasAllSitesFailed(const std::string& id);

    virtual bool needAppendSuiteName();

    void print_burstlabels();//TODO

    virtual void setD2sBlockBegin();
    virtual void setD2sBlockEnd();
    virtual unsigned long long getCurrentCycleOffset();
    virtual double getCurrentTimeStamp();
    virtual std::string getTimingPort();
    virtual double getTimingPeriod();
    virtual void wait(double timeInS);

    virtual string get_label_md5();
    virtual string get_burst_md5();
    bool isProductionMode();
protected:
    bool is_production_mode;
    d2sFrameWorkModeType::Enum currentFrameworkMode;
    std::vector<std::string> burstLabels;
    unsigned long long cycleOffset;
    std::string portName;
    bool inD2sBlock;
    int call_id;
    bool checkPassFail;
    typedef std::map<int, std::map<std::string, std::map<std::string, bool> > > sitePortIdPassFailType;
    static sitePortIdPassFailType globalPassFail;        

    string burst_md5_tag;

    string label_md5_tag;

private:
};

#endif /*TRANSACTIONPORT_H_*/
