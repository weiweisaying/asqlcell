from typing import List, Optional, TypedDict

from strenum import StrEnum


class ChartType(StrEnum):
    BAR = "bar"
    COLUMN = "column"
    LINE = "line"
    AREA = "area"
    PIE = "pie"
    SCATTER = "scatter"
    COMBO = "combo"
    FUNNEL = "funnel"


class SubChartType(StrEnum):
    CLUSTERED = "clustered"
    PERCENT = "100"


class LegendConfig(TypedDict):
    visible: bool


class AxisConfig(TypedDict):
    label: Optional[str]
    field: Optional[str]
    aggregation: Optional[str]
    sort: Optional[str]


class ChartConfig(TypedDict):
    type: Optional[ChartType]
    x: AxisConfig
    y: AxisConfig
    y2: AxisConfig
    color: AxisConfig
    subtype: List[str]
    height: int
    width: int
    legend: LegendConfig
    label: bool
