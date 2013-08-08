d1 = read.table("rssi.distance.4m.low", col.names=c("r01","r02","r03"))
d2 = read.table("rssi.distance.4m.mid", col.names=c("r11","r12","r13"))
d3 = read.table("rssi.distance.4m.high", col.names=c("r21","r22","r23"))
attach(d1)
attach(d2)
attach(d3)

x1 = seq(1, 4, by=.5)
x1range = range(x1)
y1range = range(r01, r02, r03)
y2range = range(r11, r12, r13)
y3range = range(r21, r22, r23)

cols = c("red", "green", "blue")

pdf("rssi_distance_4m.pdf", width=10, height=5)

par(mfrow=c(1,3))

plot(x1range, y1range, type="n", xlab="Distance (m)", ylab="RSSI (unitless)")
lines(x1, r01, type="b", pch=1, col=cols[1])
lines(x1, r02, type="b", pch=2, col=cols[2])
lines(x1, r03, type="b", pch=3, col=cols[3])
title("Tag at 6cm above floor level")
legend("topright", c("1 at 130cm","2 at 60cm","3 at 6cm"), pch=1:3, title="Readers", col=cols)

plot(x1range, y2range, type="n", xlab="Distance (m)", ylab="RSSI (unitless)")
lines(x1, r11, type="b", pch=1, col=cols[1])
lines(x1, r12, type="b", pch=2, col=cols[2])
lines(x1, r13, type="b", pch=3, col=cols[3])
title("Tag at 60cm above floor level")
legend("topright", c("1 at 130cm","2 at 60cm","3 at 6cm"), pch=1:3, title="Readers", col=cols)

plot(x1range, y2range, type="n", xlab="Distance (m)", ylab="RSSI (unitless)")
lines(x1, r21, type="b", pch=1, col=cols[1])
lines(x1, r22, type="b", pch=2, col=cols[2])
lines(x1, r23, type="b", pch=3, col=cols[3])
title("Tag at 130cm above floor level")
legend("topright", c("1 at 130cm","2 at 60cm","3 at 6cm"), pch=1:3, title="Readers", col=cols)

dev.off()
