FROM java:8

ENV SBT_VERSION <<SBT_VERSION>> 
ENV SCALA_VERSION <<SCALA_VERSION>> 

RUN mkdir /opt/sbt \ 
    && export REPO=http://repo.typesafe.com/typesafe/ivy-releases \ 
    && export NAMESPACE=org.scala-sbt/sbt-launch/$SBT_VERSION \ 
    && export FILE=sbt-launch.jar \ && 
    wget -O /opt/sbt/$FILE $REPO/$NAMESPACE/$FILE 

COPY sbt.sh /usr/bin/sbt 
RUN echo 'scalaVersion := "<<SCALA_VERSION>>"' > build.sbt \ 
    && sbt update \ && 
    && rm build.sbt