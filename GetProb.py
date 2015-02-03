f = open("SPAMTrain.label", "r")
lines = f.readlines()

totalMessages = 0.0
totalHamMessages = 0.0
totalSpamMessages = 0.0

for line in lines:
	totalMessages = totalMessages + 1
	flag = line.split(" ")[0]
	if flag == "1":
		totalHamMessages = totalHamMessages + 1
	else:
		totalSpamMessages = totalSpamMessages + 1


print "Total number of messages in the training set: %d" %totalMessages
print "Total number of Ham messages in the training set: %d" %totalHamMessages
print "Total number of Spam messages in the training set: %d" %totalSpamMessages
print "\n"
hamProb = totalHamMessages/totalMessages
spamProb = totalSpamMessages/totalMessages

print "P(w = Ham) = P(Ham messages) / P(Total messages) %.3f" %hamProb
print "P(w = Spam) = P(Spam messages) / P(Total messages) %.3f" %spamProb
