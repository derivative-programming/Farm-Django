import json
from datetime import date, datetime
import uuid
from decimal import Decimal
from django.db import connection
from api.reports.row_models import ReportItemLandPlantList
import logging
from api.helpers import SessionContext

class ReportProviderLandPlantList(): 
    _session_context:SessionContext
    def __init__(self, session_context:SessionContext): 
        self._session_context = session_context
    
    def generate_list(self, 
                    land_code:uuid, 
                    some_int_val: int, 
                    some_big_int_val: int, 
                    some_bit_val: bool, 
                    is_edit_allowed: bool, 
                    is_delete_allowed: bool, 
                    some_float_val: float, 
                    some_decimal_val: Decimal, 
                    some_min_utc_date_time_val: datetime, 
                    some_min_date_val: date, 
                    some_money_val: Decimal, 
                    some_n_var_char_val: str, 
                    some_var_char_val: str, 
                    some_text_val: str, 
                    some_phone_number: str, 
                    some_email_address: str, 
                    flavor_code: uuid,
                    page_number:int,
                    item_count_per_page:int,
                    order_by_column_name:str,
                    order_by_descending:bool,
                      ) -> list[dict[str,any]]: 
        
        logging.debug("ReportProviderLandPlantList.generate_list Start")
        logging.debug("ReportProviderLandPlantList.generate_list land_code:" + str(land_code))
        
        offset = (page_number - 1) * item_count_per_page

        query_dict = dict()

        query_dict["land_code"] = land_code 
        query_dict["some_int_val"] = some_int_val 
        query_dict["some_big_int_val"] = some_big_int_val 
        query_dict["some_bit_val"] = some_bit_val 
        query_dict["is_edit_allowed"] = is_edit_allowed 
        query_dict["is_delete_allowed"] = is_delete_allowed 
        query_dict["some_float_val"] = some_float_val 
        query_dict["some_decimal_val"] = some_decimal_val 
        query_dict["some_min_utc_date_time_val"] = some_min_utc_date_time_val 
        query_dict["some_min_date_val"] = some_min_date_val 
        query_dict["some_money_val"] = some_money_val 
        query_dict["some_n_var_char_val"] = some_n_var_char_val 
        query_dict["some_var_char_val"] = some_var_char_val 
        query_dict["some_text_val"] = some_text_val 
        query_dict["some_phone_number"] = some_phone_number 
        query_dict["some_email_address"] = some_email_address 
        query_dict["flavor_code"] = flavor_code 
        query_dict["page_number"] = page_number 
        query_dict["item_count_per_page"] = item_count_per_page 
        query_dict["order_by_column_name"] = order_by_column_name 
        query_dict["order_by_descending"] = order_by_descending 

        results = list()

        with connection.cursor() as cursor: 
            ##TODO report sql templates
            cursor.execute(""" 

             
	DECLARE @i_iPageNumber int = %(page_number)s
	DECLARE @i_iItemCountPerPage int = %(item_count_per_page)s
	DECLARE @i_strOrderByColumnName varchar(50) = %(order_by_column_name)s
	DECLARE @i_bOrderByDescending bit = %(order_by_descending)s
	DECLARE @i_uidUserID uniqueidentifier = %(page_number)s 
	DECLARE @i_uidContextCode uniqueidentifier = %(land_code)s 
        --GENLOOPReportParamStart
    DECLARE @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName GENVALlowercasecalculatedSqlServerDBDataSizeAndType = %(GENVALLowerUnderscoredReportParamName)s 
        --GENLOOPReportParamEnd   
	
                
        --GENLOOPReportParamStart
		--GENIF[calculatedFKObjectName=TriStateFilter]Start
		--TriStateFilter GENVALName
		DECLARE @GENVALName_TriStateFilterValue int = -1
		select @GENVALName_TriStateFilterValue = StateIntValue from TriStateFilter where code = @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName
		--GENIF[calculatedFKObjectName=TriStateFilter]End
		--GENIF[calculatedFKObjectName=DateGreaterThanFilter]Start
		--DateGreaterThanFilter GENVALName
		DECLARE @GENVALName_DateGreaterThanFilterIntValue int = -1
		select @GENVALName_DateGreaterThanFilterIntValue = DayCount from DateGreaterThanFilter where code = @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName
		DECLARE @GENVALName_DateGreaterThanFilterUtcDateTimeValue datetime = getutcdate()
		select @GENVALName_DateGreaterThanFilterUtcDateTimeValue = dateadd(d,(-1 * @GENVALName_DateGreaterThanFilterIntValue),getutcdate())
		--GENIF[calculatedFKObjectName=DateGreaterThanFilter]End
        --GENLOOPReportParamEnd

   
	SELECT * FROM 
	(
		SELECT  Top  (@i_iPageNumber * @i_iItemCountPerPage)  
        --GENLOOPReportColumnStart
		--GENIF[calculatedIsSourceObjectAvailable=true]Start
			GENVALcalculatedSourceLookupObjImplementationObjNameGENVALcalculatedSourceObjectName.GENVALLowerUnderscoredcalculatedSourcePropertyName as GENVALLowerUnderscoredReportColumnName,
		--GENIF[calculatedIsSourceObjectAvailable=true]End
		--GENIF[calculatedIsSourceObjectAvailable=false]Start
				--GENCASE[calculatedCSharpDataType]Start
				--GENWHEN[Guid]Start 
			GENVALLowerUnderscoredObjectName.code as GENVALLowerUnderscoredReportColumnName,
				--GENWHEN[Guid]End
				--GENWHEN[Boolean]Start 
				--GENIF[calculatedIsConditionalSqlLogicAvailable=false]Start 
			GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredReportColumnName as GENVALLowerUnderscoredReportColumnName,
				--GENIF[calculatedIsConditionalSqlLogicAvailable=false]End
				--GENIF[calculatedIsConditionalSqlLogicAvailable=true]Start 
			cast((case when GENVALconditionalSqlLogic then 1 else 0 end) as bit) as GENVALLowerUnderscoredReportColumnName,
				--GENIF[calculatedIsConditionalSqlLogicAvailable=true]End
				--GENWHEN[Boolean]End
				--GENElseStart  
			GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredReportColumnName as GENVALLowerUnderscoredReportColumnName,
				--GENElseEnd 
				--GENCASE[calculatedCSharpDataType]End 
		--GENIF[calculatedIsSourceObjectAvailable=false]End
		--GENLOOPReportColumnEnd  
			ROW_NUMBER() OVER(
				ORDER BY 

				
		--GENIF[calculatedIsVisualizationDetailThreeColumn=false]Start 
		--GENIF[calculatedIsVisualizationDetailTwoColumn=false]Start 
				
        --GENLOOPReportColumnStart  
				--GENFILTER[isVisible=true]  
				--GENIF[calculatedIsSourceObjectAvailable=true]Start
				--GENCASE[calculatedSqlServerDBDataType]Start
				--GENWHEN[Uniqueidentifier]Start 
				--GENWHEN[Uniqueidentifier]End
				--GENWHEN[Text]Start 
				--GENWHEN[Text]End
				--GENElseStart  
					CASE WHEN @i_bOrderByDescending = 0 and @i_strOrderByColumnName = 'GENVALReportColumnName' THEN GENVALcalculatedSourceLookupObjImplementationObjNameGENVALcalculatedSourceObjectName.GENVALLowerUnderscoredcalculatedSourcePropertyName  END ASC, 
				--GENElseEnd 
				--GENCASE[calculatedSqlServerDBDataType]End 
				--GENIF[calculatedIsSourceObjectAvailable=true]End
				--GENIF[calculatedIsSourceObjectAvailable=false]Start
				--GENCASE[calculatedSqlServerDBDataType]Start
				--GENWHEN[Uniqueidentifier]Start 
				--GENWHEN[Uniqueidentifier]End
				--GENWHEN[Text]Start 
				--GENWHEN[Text]End
				--GENElseStart  
					CASE WHEN @i_bOrderByDescending = 0 and @i_strOrderByColumnName = 'GENVALReportColumnName' THEN GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredReportColumnName  END ASC, 
				--GENElseEnd 
				--GENCASE[calculatedSqlServerDBDataType]End 
				--GENIF[calculatedIsSourceObjectAvailable=false]End 
        --GENLOOPReportColumnEnd   


        --GENLOOPReportColumnStart 
				--GENFILTER[isVisible=true]  
				--GENIF[calculatedIsSourceObjectAvailable=true]Start
				--GENCASE[calculatedSqlServerDBDataType]Start
				--GENWHEN[Uniqueidentifier]Start 
				--GENWHEN[Uniqueidentifier]End
				--GENWHEN[Text]Start 
				--GENWHEN[Text]End
				--GENElseStart  
					CASE WHEN @i_bOrderByDescending = 1 and @i_strOrderByColumnName = 'GENVALReportColumnName' THEN GENVALcalculatedSourceLookupObjImplementationObjNameGENVALcalculatedSourceObjectName.GENVALLowerUnderscoredcalculatedSourcePropertyName  END DESC, 
				--GENElseEnd 
				--GENCASE[calculatedSqlServerDBDataType]End
				--GENIF[calculatedIsSourceObjectAvailable=true]End
				--GENIF[calculatedIsSourceObjectAvailable=false]Start
				--GENCASE[calculatedSqlServerDBDataType]Start
				--GENWHEN[Uniqueidentifier]Start 
				--GENWHEN[Uniqueidentifier]End
				--GENWHEN[Text]Start 
				--GENWHEN[Text]End
				--GENElseStart  
					CASE WHEN @i_bOrderByDescending = 1 and @i_strOrderByColumnName = 'GENVALReportColumnName' THEN GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredReportColumnName  END DESC, 
				--GENElseEnd 
				--GENCASE[calculatedSqlServerDBDataType]End
				--GENIF[calculatedIsSourceObjectAvailable=false]End 
        --GENLOOPReportColumnEnd
		
		--GENIF[calculatedIsVisualizationDetailTwoColumn=false]End 
		--GENIF[calculatedIsVisualizationDetailThreeColumn=false]End 

					CASE WHEN @i_bOrderByDescending = 1 and @i_strOrderByColumnName = 'placeholder' THEN ''  END DESC 

				) AS ROWNUMBER 
		  -- select * 
		from 
		 	api_GENVALLowerUnderscoredObjectName  GENVALLowerUnderscoredObjectName  --owner obj
			
			--GENIF[calculatedIsTargetChildObjectAvailable=true]Start
			--GENIF[calculatedIsTrueParentChild=false]Start
			--left join api_GENVALcalculatedTargetChildObject GENVALcalculatedTargetChildObject on 1=1			
			--GENIF[calculatedIsTrueParentChild=false]End
			--GENIF[calculatedIsTrueParentChild=true]Start
			  join api_GENVALcalculatedTargetChildObject GENVALcalculatedTargetChildObject on GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredObjectName_id = GENVALcalculatedTargetChildObject.GENVALLowerUnderscoredObjectName_id		 --child obj
			--GENLOOPchildObjLookupsSTART
			left join api_GENVALlookupName GENVALcalculatedTargetChildObjectGENVALlookupName on GENVALcalculatedTargetChildObject.GENVALimplementationPropName = GENVALcalculatedTargetChildObjectGENVALlookupName.GENVALLowerUnderscoredlookupName_id --child obj lookup prop
			--GENLOOPchildObjLookupsEnd 
			--GENIF[calculatedIsTrueParentChild=true]End 
			--GENIF[calculatedIsTargetChildObjectAvailable=true]End
			
			--GENLOOPPropSTART
			--GENIF[isFK=true]Start
			--GENIF[calculatedisFKObjectParentOFOwnerObject=false]Start
			--GENIF[isFKLookup=false]Start
			left join api_GENVALPROPcalculatedFKObjectName GENVALPROPcalculatedFKObjectName on GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredPropName = GENVALPROPcalculatedFKObjectName.GENVALLowerUnderscoredPROPcalculatedFKObjectPropertyName   -- fk prop
			--GENIF[isFKLookup=false]End
			--GENIF[isFKLookup=true]Start
			left join api_GENVALPROPcalculatedFKObjectName GENVALLowerUnderscoredObjectNameGENVALPROPcalculatedFKObjectName on GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredPropName = GENVALLowerUnderscoredObjectNameGENVALPROPcalculatedFKObjectName.GENVALLowerUnderscoredPROPcalculatedFKObjectPropertyName   -- fk prop
			--GENIF[isFKLookup=true]End
			--GENIF[calculatedisFKObjectParentOFOwnerObject=false]End  
			--GENIF[isFK=true]End 
			--GENLOOPPropEnd  
			
			--GENLOOPobjTreePathSTART   
			left join api_GENVALparentObjName GENVALparentObjName on GENVALparentObjName.GENVALLowerUnderscoredparentObjName_id = GENVALchildObjName.GENVALchildPropName  -- up obj tree
			--GENLOOPparentObjLookupsSTART   
			left join api_GENVALlookupName GENVALparentObjNameGENVALlookupName on GENVALparentObjName.GENVALimplementationPropName = GENVALparentObjNameGENVALlookupName.GENVALLowerUnderscoredlookupName_id -- tree parent obj lookup prop
			--GENLOOPparentObjLookupsEnd 
			--GENLOOPobjTreePathEnd 
			 

			--GENLOOPobjJoinTreeSTART   
			left join api_GENVALchildObjName GENVALchildObjName on GENVALchildObjName.GENVALchildPropName = GENVALparentObjName.GENVALLowerUnderscoredparentObjName_id  -- up obj join tree
			--GENLOOPchildObjLookupsSTART   
			left join api_GENVALlookupName GENVALchildObjNameGENVALlookupName on GENVALchildObjName.GENVALimplementationPropName = GENVALchildObjNameGENVALlookupName.GENVALLowerUnderscoredlookupName_id -- join tree hild obj lookup prop
			--GENLOOPchildObjLookupsEnd 
			--GENLOOPobjJoinTreeEnd 
			
			--GENIF[calculatedIsTargetChildObjAPairedIntersectionObj=true]Start
			--GENLOOPintersectionObjSTART 
			--owner obj intersection table  
			join  api_GENVALLowerUnderscoredName GENVALLowerUnderscoredName on GENVALLowerUnderscoredName.GENVALLowerUnderscoredObjectName_id = GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredObjectName_id
			join api_GENVALpairedObj GENVALpairedObj on GENVALLowerUnderscoredName.GENVALLowerUnderscoredpairedObj_id = GENVALpairedObj.GENVALLowerUnderscoredpairedObj_id
			--GENLOOPintersectionObjEnd
			--GENIF[calculatedIsTargetChildObjAPairedIntersectionObj=true]End
			
			
			--GENIF[calculatedIsTargetChildObjAPairedIntersectionObj=false]Start
			--GENLOOPintersectionObjSTART 
			--owner obj intersection table , 1st record only
			left join api_GENVALLowerUnderscoredName GENVALLowerUnderscoredName on GENVALLowerUnderscoredName.GENVALLowerUnderscoredObjectName_id = GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredObjectName_id
			left join api_GENVALLowerUnderscoredName GENVALLowerUnderscoredName2 on GENVALLowerUnderscoredName.GENVALLowerUnderscoredObjectName_id = GENVALLowerUnderscoredName2.GENVALLowerUnderscoredObjectName_id and GENVALLowerUnderscoredName.GENVALLowerUnderscoredName_id > GENVALLowerUnderscoredName2.GENVALLowerUnderscoredName_id
			--GENLOOPintersectionObjEnd
			--GENIF[calculatedIsTargetChildObjAPairedIntersectionObj=false]End
			
			
			--GENLOOPtargetChildObjectIntersectionObjSTART 
			--target child obj intersection table , 1st record only
			left join api_GENVALLowerUnderscoredName GENVALLowerUnderscoredName on GENVALLowerUnderscoredName.GENVALcalculatedTargetChildObjectID = GENVALcalculatedTargetChildObject.GENVALcalculatedTargetChildObjectID
			left join api_GENVALLowerUnderscoredName GENVALLowerUnderscoredName2 on GENVALLowerUnderscoredName.GENVALcalculatedTargetChildObjectID = GENVALLowerUnderscoredName2.GENVALcalculatedTargetChildObjectID and GENVALLowerUnderscoredName.GENVALLowerUnderscoredName_id > GENVALLowerUnderscoredName2.GENVALLowerUnderscoredName_id
			--left join api_GENVALpairedObj GENVALpairedObj on GENVALLowerUnderscoredName.GENVALLowerUnderscoredpairedObj_id = GENVALpairedObj.GENVALpairedObjID
			--GENLOOPtargetChildObjectIntersectionObjEnd
			
			--GENIF[calculatedIsRowLevelOrgCustomerSecurityUsed=true]Start 
			join api_Customer Customer_Security on orgCustomer.CustomerID = Customer_Security.CustomerID
			--GENIF[calculatedIsRowLevelOrgCustomerSecurityUsed=true]End
			
			--GENIF[calculatedIsRowLevelOrganizationSecurityUsed=true]Start
			join api_OrgCustomer orgCustomer_Security on orgCustomer_Security.OrganizationID = Organization.OrganizationID
			join api_Customer Customer_Security on orgCustomer_Security.CustomerID = Customer_Security.CustomerID
			--GENIF[calculatedIsRowLevelOrganizationSecurityUsed=true]End

		where
			 (GENVALLowerUnderscoredObjectName.code = @i_uidContextCode 
			 GENVALfilteringSqlLogic  )
			--GENIF[calculatedIsRowLevelCustomerSecurityUsed=true]Start
			and (@i_uidUserID is not null and @i_uidUserID <> '00000000-0000-0000-0000-000000000000' and Customer.Code = @i_uidUserID )
			--GENIF[calculatedIsRowLevelCustomerSecurityUsed=true]End

			--GENIF[calculatedIsRowLevelOrgCustomerSecurityUsed=true]Start
			and (@i_uidUserID is not null and @i_uidUserID <> '00000000-0000-0000-0000-000000000000' and Customer_Security.Code = @i_uidUserID )
			--GENIF[calculatedIsRowLevelOrgCustomerSecurityUsed=true]End

			--GENIF[calculatedIsRowLevelOrganizationSecurityUsed=true]Start
			and (@i_uidUserID is not null and @i_uidUserID <> '00000000-0000-0000-0000-000000000000' and Customer_Security.Code = @i_uidUserID )
			--GENIF[calculatedIsRowLevelOrganizationSecurityUsed=true]End
			 
			--GENIF[calculatedIsTargetChildObjAPairedIntersectionObj=false]Start
			--GENLOOPintersectionObjSTART  
			and GENVALLowerUnderscoredName2.GENVALLowerUnderscoredName_id is null
			--GENLOOPintersectionObjEnd
			--GENIF[calculatedIsTargetChildObjAPairedIntersectionObj=false]End
			
			--GENLOOPtargetChildObjectIntersectionObjSTART 
			and GENVALLowerUnderscoredName2.GENVALLowerUnderscoredName_id is null
			--GENLOOPtargetChildObjectIntersectionObjEnd

        --GENLOOPReportParamStart 
		--GENIF[calculatedIsTargetObjectAvailable=true]Start
			 	--GENCASE[calculatedCSharpDataType]Start
				--GENWHEN[String]Start 
			and (@i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName is null or @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName = GENVALcalculatedSqlServerSingleQuoteDefaultValue or  GENVALcalculatedTargetLookupObjImplementationObjNameGENVALcalculatedTargetObjectName.GENVALcalculatedTargetPropertyName like '%' + @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName + '%')
				--GENWHEN[String]End
				--GENElseStart  
				
				--GENIF[calculatedFKObjectName=TriStateFilter]Start
				--TriStateFilter GENVALName @GENVALName_TriStateFilterValue
			and (@i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName is null or @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName = '00000000-0000-0000-0000-000000000000' or @GENVALName_TriStateFilterValue = -1 or @GENVALName_TriStateFilterValue = GENVALcalculatedTargetLookupObjImplementationObjNameGENVALcalculatedTargetObjectName.GENVALcalculatedTargetPropertyName)
				--GENIF[calculatedFKObjectName=TriStateFilter]End
				--GENIF[calculatedFKObjectName=DateGreaterThanFilter]Start
				--DateGreaterThanFilter GENVALName @GENVALName_DateGreaterThanFilterUtcDateTimeValue
			and (@i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName is null or @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName = '00000000-0000-0000-0000-000000000000' or @GENVALName_DateGreaterThanFilterUtcDateTimeValue < GENVALcalculatedTargetLookupObjImplementationObjNameGENVALcalculatedTargetObjectName.GENVALcalculatedTargetPropertyName)
				--GENIF[calculatedFKObjectName=DateGreaterThanFilter]End
				
				--GENIF[calculatedFKObjectName!=TriStateFilter]Start
				--GENIF[calculatedFKObjectName!=DateGreaterThanFilter]Start
			and (@i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName is null or @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName = GENVALcalculatedSqlServerSingleQuoteDefaultValue or @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALLowerUnderscoredReportParamName = GENVALcalculatedTargetLookupObjImplementationObjNameGENVALcalculatedTargetObjectName.GENVALcalculatedTargetPropertyName)
				--GENIF[calculatedFKObjectName!=DateGreaterThanFilter]End
				--GENIF[calculatedFKObjectName!=TriStateFilter]End

				--GENElseEnd 
				--GENCASE[calculatedCSharpDataType]End
		--GENIF[calculatedIsTargetObjectAvailable=true]End
		--GENIF[calculatedIsTargetObjectAvailable=false]Start
			 	--GENCASE[calculatedCSharpDataType]Start
				--GENWHEN[String]Start 
			and (@i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName is null or @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName = GENVALcalculatedSqlServerSingleQuoteDefaultValue or  GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredReportParamName like '%' + @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALLowerUnderscoredReportParamName + '%')
				--GENWHEN[String]End
				--GENElseStart  
			and (@i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName is null or @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALReportParamName = GENVALcalculatedSqlServerSingleQuoteDefaultValue or @i_GENVALCamelcalculatedDBStoredProcParameterPrefixGENVALLowerUnderscoredReportParamName = GENVALLowerUnderscoredObjectName.GENVALLowerUnderscoredReportParamName)
				--GENElseEnd 
				--GENCASE[calculatedCSharpDataType]End
		--GENIF[calculatedIsTargetObjectAvailable=false]End
        --GENLOOPReportParamEnd    
   
	) AS TBL
	WHERE 
		ROWNUMBER BETWEEN ((@i_iPageNumber - 1) * @i_iItemCountPerPage + 1) AND (@i_iPageNumber * @i_iItemCountPerPage) 
		  
                """, query_dict)
            results = self.dictfetchall(cursor)
             
        logging.debug("ReportProviderLandPlantList.generate_list Results: " + json.dumps(results))

        logging.debug("ReportProviderLandPlantList.generate_list End")
        return results

    def dictfetchall(self, cursor) -> list[dict[str,any]]:
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]