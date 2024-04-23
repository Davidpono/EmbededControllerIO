from AddIOP import AddIOP
from getmax import getmaxmin


def AO(type, iopin, COVIncrement, MaxPresValue, MinPresValue, VarName, Description,offset, ElecTopOfScale, EngBottomOfScale, EngTopOfScale,ThermistorType,ActiveText,InactiveText,newxmlIOfolder):
        
        ElecTopOfScale, ElecBottomOfScale=getmaxmin(ThermistorType)
        insert=f'''<OI DESCR="Chilled Water Valve Command" NAME="{VarName}" TYPE="bacnet.mpx.point.VoltageOutput" flags="libExcluded">
      <PI Name="BACnetName" Value="{VarName}"/>
      <PI Name="COVIncrement" Unit="0x200001" Value="{COVIncrement}"/>
      <PI Name="ElecBottomOfScale" Value="{ElecBottomOfScale}"/>
      <PI Name="ElecTopOfScale" Value="{ElecTopOfScale}"/>
      <PI Name="EngBottomOfScale" Unit="0x200001" Value="{EngBottomOfScale}"/>
      <PI Name="EngTopOfScale" Unit="0x200001" Value="{EngTopOfScale}"/>
      <PI Name="ForeignAddress" Value="&lt;analog-output,     628&gt;"/>
      <PI Name="MaxPresValue" Unit="0x200001" Value="{MaxPresValue}"/>
      <PI Name="MinPresValue" Unit="0x200001" Value="{MinPresValue}"/>
      <PI Name="Priority10" VariableReference="Application">
        <Reference DeltaFilter="0" Object="../../../Programs/{VarName}Ctrl" Property="{VarName}_p10" Retransmit="0" TransferRate="10"/>
      </PI>
      <PI Name="Terminal">
        <Reference DeltaFilter="0" Object="../../../../IO Resources/Onboard IO/{iopin}" Retransmit="0" TransferRate="10"/>
      </PI>
      <PI Name="Value" Unit="0x200001"/>
    </OI>
        '''
        AddIOP( insert,newxmlIOfolder)
       
        