classdef NodeGroup
    properties
        satcat
        types
        times
        signals
        firsttime
        lasttime
        num
        num_IDs
        num_ADs
        num_IKs
        duration
    end
    
    methods
        function obj = NodeGroup(satcat, types, times, signals)
            obj.satcat = str2double(satcat);
            obj.types = types;
            obj.times = times;
            obj.signals = signals;
            
            if ~isempty(times)
                obj.firsttime = times(1);
                obj.lasttime = times(end);
                obj.duration = times(end) - times(1);
            else
                obj.firsttime = [];
                obj.lasttime = [];
                obj.duration = duration(5, 0, 0); % Default duration of 5 days
            end
            
            obj.num = length(types);
            
            % Count occurrences of each type
            icount = sum(strcmp(types, 'ID'));
            acount = sum(strcmp(types, 'AD'));
            ecount = sum(strcmp(types, 'IK'));
            
            obj.num_IDs = icount;
            obj.num_ADs = acount;
            obj.num_IKs = ecount;
        end
    end
end