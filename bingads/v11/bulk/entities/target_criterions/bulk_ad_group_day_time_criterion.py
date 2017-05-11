from bingads.v11.bulk.entities import *
from bingads.service_client import _CAMPAIGN_OBJECT_FACTORY_V11
from bingads.v11.internal.bulk.entities.single_record_bulk_entity import _SingleRecordBulkEntity
from bingads.v11.internal.bulk.mappings import _SimpleBulkMapping
from bingads.v11.internal.bulk.string_table import _StringTable
from bingads.internal.extensions import *

class BulkAdGroupDayTimeCriterion(_SingleRecordBulkEntity):
    """ Represents an Ad Group Day Time Criterion that can be read or written in a bulk file.

    This class exposes the :attr:`ad_group_criterion` property that can be read and written as fields of the
    Ad Group Day Time Criterion record in a bulk file.

    For more information, see Ad Group Day Time Criterion at https://go.microsoft.com/fwlink/?linkid=846127.

    *See also:*

    * :class:`.BulkServiceManager`
    * :class:`.BulkOperation`
    * :class:`.BulkFileReader`
    * :class:`.BulkFileWriter`
    """

    def __init__(self,
                 ad_group_criterion=None,
                 campaign_name=None,
                 ad_group_name=None, ):
        super(BulkAdGroupDayTimeCriterion, self).__init__()

        self._ad_group_criterion = ad_group_criterion
        self._campaign_name = campaign_name
        self._ad_group_name =ad_group_name

    _MAPPINGS = [
        _SimpleBulkMapping(
            _StringTable.Status,
            field_to_csv=lambda c: bulk_str(c.ad_group_criterion.Status),
            csv_to_field=lambda c, v: setattr(c.ad_group_criterion, 'Status', v if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.Id,
            field_to_csv=lambda c: bulk_str(c.ad_group_criterion.Id),
            csv_to_field=lambda c, v: setattr(c.ad_group_criterion, 'Id', int(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.ParentId,
            field_to_csv=lambda c: bulk_str(c.ad_group_criterion.AdGroupId),
            csv_to_field=lambda c, v: setattr(c.ad_group_criterion, 'AdGroupId', int(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.Campaign,
            field_to_csv=lambda c: c.campaign_name,
            csv_to_field=lambda c, v: setattr(c, 'campaign_name', v)
        ),
        _SimpleBulkMapping(
            _StringTable.AdGroup,
            field_to_csv=lambda c: c.ad_group_name,
            csv_to_field=lambda c, v: setattr(c, 'ad_group_name', v)
        ),
        _SimpleBulkMapping(
            _StringTable.BidAdjustment,
            field_to_csv=lambda c: field_to_csv_BidAdjustment(c.ad_group_criterion),
            csv_to_field=lambda c, v: csv_to_field_BidAdjustment(c.ad_group_criterion, float(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.Target,
            field_to_csv=lambda c: field_to_csv_DayTimeTarget(c.ad_group_criterion),
            csv_to_field=lambda c, v: csv_to_field_DayTimeTarget(c.ad_group_criterion, v)
        ),
        _SimpleBulkMapping(
            _StringTable.FromHour,
            field_to_csv=lambda c: field_to_csv_FromHour(c.ad_group_criterion),
            csv_to_field=lambda c, v: csv_to_field_FromHour(c.ad_group_criterion, int(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.FromMinute,
            field_to_csv=lambda c: field_to_csv_FromMinute(c.ad_group_criterion),
            csv_to_field=lambda c, v: csv_to_field_FromMinute(c.ad_group_criterion, v)
        ),
        _SimpleBulkMapping(
            _StringTable.ToHour,
            field_to_csv=lambda c: field_to_csv_ToHour(c.ad_group_criterion),
            csv_to_field=lambda c, v: csv_to_field_ToHour(c.ad_group_criterion, int(v) if v else None)
        ),
        _SimpleBulkMapping(
            _StringTable.ToMinute,
            field_to_csv=lambda c: field_to_csv_ToMinute(c.ad_group_criterion),
            csv_to_field=lambda c, v: csv_to_field_ToMinute(c.ad_group_criterion, v)
        ),
    ]

    @property
    def ad_group_criterion(self):
        """ Defines a Ad Group Criterion """

        return self._ad_group_criterion

    @ad_group_criterion.setter
    def ad_group_criterion(self, ad_group_criterion):
        self._ad_group_criterion = ad_group_criterion

    @property
    def campaign_name(self):
        """ The name of the Campaign

        :rtype: str
        """

        return self._campaign_name

    @campaign_name.setter
    def campaign_name(self, campaign_name):
        self._campaign_name = campaign_name

    @property
    def ad_group_name(self):
        """ The name of the Ad Group

        :rtype: str
        """

        return self._ad_group_name

    @ad_group_name.setter
    def ad_group_name(self, ad_group_name):
        self._ad_group_name = ad_group_name


    def process_mappings_to_row_values(self, row_values, exclude_readonly_data):
        self._validate_property_not_null(self.ad_group_criterion, 'ad_group_criterion')
        self.convert_to_values(row_values, BulkAdGroupDayTimeCriterion._MAPPINGS)

    def process_mappings_from_row_values(self, row_values):
        self._ad_group_criterion = _CAMPAIGN_OBJECT_FACTORY_V11.create('BiddableAdGroupCriterion')
        self._ad_group_criterion.Type = 'BiddableAdGroupCriterion'
        self._ad_group_criterion.Criterion = _CAMPAIGN_OBJECT_FACTORY_V11.create('DayTimeCriterion')
        self._ad_group_criterion.Criterion.Type = 'DayTimeCriterion'
        self._ad_group_criterion.CriterionBid = _CAMPAIGN_OBJECT_FACTORY_V11.create('BidMultiplier')
        self._ad_group_criterion.CriterionBid.Type = 'BidMultiplier'
        row_values.convert_to_entity(self, BulkAdGroupDayTimeCriterion._MAPPINGS)

    def read_additional_data(self, stream_reader):
        super(BulkAdGroupDayTimeCriterion, self).read_additional_data(stream_reader)
