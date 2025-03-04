import { Stack, Text } from "@mantine/core";
import React, { FunctionComponent } from "react";
import { AggregationSwitch, FieldSwitch } from "./properties";

export const ColumnChart: FunctionComponent = () => {
    return (
        <Stack>
            <Text fw={600}>X-Axis</Text>

            <FieldSwitch major="x" minor="y" sort />

            <Text fw={600}>Y-Axis</Text>

            <FieldSwitch major="y" minor="x" sort />

            <AggregationSwitch major="y" minor="x" />

            <FieldSwitch major="color" clearable />
        </Stack>
    );
}
